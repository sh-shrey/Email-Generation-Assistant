import re
import json
import openai
from email_assistant import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


# METRIC 1: FACT RECALL SCORE


def _extract_facts_from_string(facts_str: str) -> list[str]:
    facts = [f.strip() for f in facts_str.split(";") if f.strip()]
    return facts


def _fact_present_in_email(fact: str, email_body: str) -> bool:
    email_lower = email_body.lower()
    fact_lower  = fact.lower()

    tokens = re.findall(r'\$[\d,]+|\d+[\w%/]*|[a-zA-Z]{4,}', fact_lower)

    if not tokens:
        return False

    matches = sum(1 for t in tokens if t in email_lower)
    return (matches / len(tokens)) >= 0.5


def metric_fact_recall(facts_str: str, generated_email: str) -> dict:
    facts = _extract_facts_from_string(facts_str)
    detail = []
    found_count = 0

    for fact in facts:
        found = _fact_present_in_email(fact, generated_email)
        if found:
            found_count += 1
        detail.append({"fact": fact, "found": found})

    total = len(facts) if facts else 1
    score = round(found_count / total, 4)

    return {
        "score": score,
        "facts_found": found_count,
        "total_facts": total,
        "detail": detail,
    }


# METRIC 2 : Tone Alignment Score (LLM-as-Judge)


TONE_JUDGE_PROMPT = """You are a professional email evaluator. You will be given:
1. The REQUESTED TONE for an email
2. The GENERATED EMAIL

Your task: Rate how accurately the email's tone, word choice, and emotional register match the requested tone on a scale from 1 to 10.

Scoring guide:
10 — Perfect match; every sentence feels exactly like the requested tone
8–9 — Very strong match; minor occasional deviations
6–7 — Good match overall but noticeable inconsistencies
4–5 — Partially aligned; significant portions miss the tone
2–3 — Mostly misaligned; only superficial attempts at the tone
1   — Completely wrong tone

Respond ONLY with a JSON object in this exact format (no preamble, no explanation):
{"score": <integer 1-10>, "reason": "<one concise sentence explaining the score>"}"""


def metric_tone_alignment(requested_tone: str, generated_email: str) -> dict:
    user_message = (
        f"REQUESTED TONE: {requested_tone}\n\n"
        f"GENERATED EMAIL:\n{generated_email}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": TONE_JUDGE_PROMPT},
            {"role": "user",   "content": user_message},
        ],
        temperature=0,
        max_tokens=150,
    )

    raw_text = response.choices[0].message.content.strip()

    raw_text = re.sub(r"```(?:json)?", "", raw_text).strip().rstrip("```").strip()

    try:
        parsed    = json.loads(raw_text)
        raw_score = int(parsed.get("score", 5))
        reason    = parsed.get("reason", "")
    except Exception:
        raw_score = 5
        reason    = "Parse error — defaulting to 5"

    return {
        "score":     round(raw_score / 10, 4),
        "raw_score": raw_score,
        "reason":    reason,
    }


# METRIC 3: CLARITY & CONCISENESS SCORE (Hybrid)


CLARITY_JUDGE_PROMPT = """You are an expert business writing critic. Evaluate the following email on CLARITY and FLUENCY:
- Is the language clear and easy to understand?
- Are sentences well-structured with no grammatical errors?
- Does the email flow logically from opening to close?
- Is there any redundancy, padding, or awkward phrasing?

Rate on a scale of 1 to 10:
10 — Flawlessly clear, every word earns its place
8–9 — Very clear with minor issues
6–7 — Generally clear but some awkward phrasing or redundancy
4–5 — Noticeable clarity issues that distract the reader
1–3 — Poorly written; confusing or grammatically flawed

Respond ONLY with JSON (no preamble):
{"score": <integer 1-10>, "reason": "<one concise sentence>"}"""


def _count_words(text: str) -> int:
    return len(text.split())


def _length_component(word_count: int) -> float:
    if 100 <= word_count <= 280:
        return 1.0
    elif word_count < 80:
        return max(0.0, round(word_count / 80, 4))
    else:  
        penalty = (word_count - 280) / 280
        return max(0.0, round(1.0 - penalty, 4))


def metric_clarity_conciseness(generated_email: str) -> dict:
   
    word_count      = _count_words(generated_email)
    length_score    = _length_component(word_count)

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": CLARITY_JUDGE_PROMPT},
            {"role": "user",   "content": f"EMAIL:\n{generated_email}"},
        ],
        temperature=0,
        max_tokens=150,
    )

    raw_text = response.choices[0].message.content.strip()
    raw_text = re.sub(r"```(?:json)?", "", raw_text).strip().rstrip("```").strip()

    try:
        parsed    = json.loads(raw_text)
        llm_raw   = int(parsed.get("score", 7))
        reason    = parsed.get("reason", "")
    except Exception:
        llm_raw = 7
        reason  = "Parse error — defaulting to 7"

    llm_norm     = round(llm_raw / 10, 4)
    final_score  = round(0.4 * length_score + 0.6 * llm_norm, 4)

    return {
        "score":                 final_score,
        "length_component":      length_score,
        "llm_clarity_raw":       llm_raw,
        "llm_clarity_normalised":llm_norm,
        "word_count":            word_count,
        "reason":                reason,
    }


# COMBINED EVALUATOR

def evaluate_email(scenario: dict, generated_email: str) -> dict:
    """
    Run all 3 metrics on a single generated email.
    Returns a flat result dict ready for CSV/JSON export.
    """
    m1 = metric_fact_recall(scenario["facts"], generated_email)
    m2 = metric_tone_alignment(scenario["tone"], generated_email)
    m3 = metric_clarity_conciseness(generated_email)

    overall = round((m1["score"] + m2["score"] + m3["score"]) / 3, 4)

    return {
        "scenario_id":            scenario["id"],
        "intent":                 scenario["intent"],
        "tone":                   scenario["tone"],
        # Metric 1
        "fact_recall_score":      m1["score"],
        "facts_found":            m1["facts_found"],
        "total_facts":            m1["total_facts"],
        # Metric 2
        "tone_alignment_score":   m2["score"],
        "tone_raw_score":         m2["raw_score"],
        "tone_reason":            m2["reason"],
        # Metric 3
        "clarity_conciseness_score": m3["score"],
        "word_count":             m3["word_count"],
        "clarity_llm_raw":        m3["llm_clarity_raw"],
        "clarity_reason":         m3["reason"],
        # Overall
        "overall_score":          overall,
        "generated_email":        generated_email,
    }
