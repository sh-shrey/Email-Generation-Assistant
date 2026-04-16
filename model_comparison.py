
import csv
import json
import time
import statistics
from email_assistant import generate_email
from evaluator import evaluate_email
from eval_scenarios import SCENARIOS

MODELS = {
    "gpt-4o":        "Model_A_GPT4o",
    "gpt-3.5-turbo": "Model_B_GPT35",
}

OUTPUT_CSV  = "evaluation_results.csv"
OUTPUT_JSON = "evaluation_results.json"


def run_evaluation(model_key: str, model_label: str) -> list[dict]:
    print(f"\n{'='*60}")
    print(f"  Running evaluation for: {model_label} ({model_key})")
    print(f"{'='*60}")

    results = []

    for scenario in SCENARIOS:
        print(f"  Scenario {scenario['id']:02d} - {scenario['intent'][:55]}...")

        generated = generate_email(
            intent=scenario["intent"],
            facts=scenario["facts"],
            tone=scenario["tone"],
            model=model_key,
        )

        # Evaluate
        result = evaluate_email(scenario, generated)
        result["model"] = model_label
        results.append(result)

        time.sleep(2)

    return results


def save_results(all_results: list[dict]) -> None:
    # ----- CSV -----
    if not all_results:
        print("No results to save.")
        return

    fieldnames = [
        "model", "scenario_id", "intent", "tone",
        "fact_recall_score", "facts_found", "total_facts",
        "tone_alignment_score", "tone_raw_score", "tone_reason",
        "clarity_conciseness_score", "word_count",
        "clarity_llm_raw", "clarity_reason",
        "overall_score",
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_results)

    print(f"\n  CSV saved -> {OUTPUT_CSV}")

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    print(f"  JSON saved -> {OUTPUT_JSON}")


def print_summary(all_results: list[dict]) -> None:
    print("\n" + "="*70)
    print("  EVALUATION SUMMARY")
    print("="*70)

    for model_label in MODELS.values():
        subset = [r for r in all_results if r["model"] == model_label]
        if not subset:
            continue

        f1_scores   = [r["fact_recall_score"]          for r in subset]
        tone_scores = [r["tone_alignment_score"]        for r in subset]
        clar_scores = [r["clarity_conciseness_score"]   for r in subset]
        overall     = [r["overall_score"]               for r in subset]

        print(f"\n  {model_label}")
        print(f"    Fact Recall         avg: {statistics.mean(f1_scores):.4f}  "
              f"min: {min(f1_scores):.4f}  max: {max(f1_scores):.4f}")
        print(f"    Tone Alignment      avg: {statistics.mean(tone_scores):.4f}  "
              f"min: {min(tone_scores):.4f}  max: {max(tone_scores):.4f}")
        print(f"    Clarity/Conciseness avg: {statistics.mean(clar_scores):.4f}  "
              f"min: {min(clar_scores):.4f}  max: {max(clar_scores):.4f}")
        print(f"    -------------------------------------------------")
        print(f"    OVERALL             avg: {statistics.mean(overall):.4f}")

    print("\n" + "="*70)


def main():
    all_results = []

    for model_key, model_label in MODELS.items():
        results = run_evaluation(model_key, model_label)
        all_results.extend(results)

    save_results(all_results)
    print_summary(all_results)

    print("\n  Done! Check evaluation_results.csv and evaluation_results.json")


if __name__ == "__main__":
    main()
