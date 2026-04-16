# Email Generation Assistant

A full end-to-end prototype that generates professional business emails using advanced prompt engineering, evaluates output quality with three custom metrics, and compares two OpenAI models side-by-side.

---

## Project Structure

```
email_assistant/
├── email_assistant.py      # Core generator — advanced prompt template
├── eval_scenarios.py       # 10 test scenarios + human reference emails
├── evaluator.py            # 3 custom evaluation metrics
├── model_comparison.py     # Runs both models, saves results
├── run_all.py              # Single entry point
├── final_report.md         # Full written report
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## Quick Start

### 1. Prerequisites

- Python 3.11+
- An OpenAI API key with access to `gpt-4o` and `gpt-3.5-turbo`

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your OpenAI API Key (recommended: `.env`)

Set `OPENAI_API_KEY` as an environment variable or place it in a `.env` file.

Example `.env`:

```bash
OPENAI_API_KEY="sk-...your-key..."
```

> All files use the same key via `email_assistant.py`, which reads `OPENAI_API_KEY` from your environment (and auto-loads `.env` if present).

### 4. Run the full pipeline

```bash
cd TASK
python run_all.py
```

This will:
1. Run a quick smoke test (1 email)
2. Generate emails for all 10 scenarios × 2 models = 20 emails
3. Evaluate each with all 3 custom metrics (~40 additional LLM calls)
4. Save `evaluation_results.csv` and `evaluation_results.json`
5. Print a summary table to the console

**Estimated runtime:** 3–6 minutes, ~60 total API calls.

---

## Running Individual Components

```bash
# Test just the email generator
python email_assistant.py

# Run only the comparison + evaluation
python model_comparison.py
```

---

## Advanced Prompting Techniques Used

The system prompt in `email_assistant.py` combines three techniques:

| Technique | How it's used |
|---|---|
| **Role-Playing** | The model is assigned the persona of "EmailCraft Pro," an elite corporate communications specialist, which consistently elevates vocabulary and structure |
| **Few-Shot Examples** | Two complete, annotated input→output examples are embedded directly in the system prompt |
| **Chain-of-Thought** | The model is instructed to follow a 5-step internal reasoning process (Analyse → Assess → Structure → Embed → Review) before generating output |

---

## Custom Evaluation Metrics

### Metric 1 — Fact Recall Score (`fact_recall_score`)
**Type:** Automated (regex/token matching)  
**Logic:** The facts string is split by semicolons into individual fact phrases. For each fact, key tokens (words ≥ 4 chars + numeric/dollar values) are extracted and checked against the generated email body. A fact is considered "recalled" if ≥ 50% of its key tokens appear in the email. Score = `facts_found / total_facts` (0.0–1.0).

### Metric 2 — Tone Alignment Score (`tone_alignment_score`)
**Type:** LLM-as-Judge (GPT-4o)  
**Logic:** A strict judge prompt asks GPT-4o to rate how accurately the generated email's tone matches the requested tone on a 1–10 scale. The raw score is normalised to 0.0–1.0. The model is given detailed rubric anchors for each score tier to ensure consistent ratings.

### Metric 3 — Clarity & Conciseness Score (`clarity_conciseness_score`)
**Type:** Hybrid (automated length check + LLM fluency rating)  
**Logic:**  
- **Length component (40%):** Ideal email = 100–280 words. Emails outside this range receive a proportional penalty.  
- **LLM clarity component (60%):** GPT-4o rates grammatical fluency, logical flow, and absence of redundancy on a 1–10 scale.  
- `Final = 0.4 × length_score + 0.6 × llm_clarity_normalised`

**Overall Score** = simple average of all three metric scores.

---

## Output Files

| File | Contents |
|---|---|
| `evaluation_results.csv` | All scores, per-scenario, per-model — importable to Excel/Sheets |
| `evaluation_results.json` | Full results including generated emails and judge reasoning |

---

## Cost Estimate

Running the full pipeline makes approximately:
- 20 generation calls (10 scenarios × 2 models)
- 20 tone-judge calls
- 20 clarity-judge calls

Total: ~60 API calls. At standard GPT-4o pricing this costs approximately **$0.30–$0.80** depending on response lengths.

---

## Notes

- The evaluator uses `gpt-4o` as the judge for both models to ensure a neutral, consistent referee.
- All LLM judge calls use `temperature=0` for deterministic scoring.
- A 2-second sleep between API calls prevents rate-limit errors.
