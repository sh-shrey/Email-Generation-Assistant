import os
import sys

def check_api_key():
    try:
        from email_assistant import OPENAI_API_KEY
    except RuntimeError as e:
        print("ERROR: OpenAI API key missing.")
        print("Set OPENAI_API_KEY in your environment or in a .env file, then re-run.")
        print(f"Details: {e}")
        sys.exit(1)

    if not OPENAI_API_KEY:
        print("ERROR: OpenAI API key missing (OPENAI_API_KEY is empty).")
        print("Set OPENAI_API_KEY in your environment or in a .env file, then re-run.")
        sys.exit(1)

    print("[OK] API key detected")


def main():
    print("=" * 60)
    print("  EMAIL GENERATION ASSISTANT - FULL PIPELINE")
    print("=" * 60)

    check_api_key()

    print("\n[1/2] Running smoke test on single scenario...")
    from email_assistant import generate_email
    test_email = generate_email(
        intent="Thank a client for their business",
        facts="Client: Apex Corp; relationship: 2 years; recent project: CRM overhaul; project outcome: 40% efficiency gain",
        tone="Warm, professional",
        model="gpt-4o",
    )
    print("\n--- Sample Email ---")
    print(test_email[:500], "...(truncated)" if len(test_email) > 500 else "")

    print("\n[2/2] Running full model comparison evaluation...")
    print("This will make ~60 API calls (~20 generations + ~40 evaluation calls).")
    print("Estimated time: 3-6 minutes.\n")

    from model_comparison import main as run_comparison
    run_comparison()

    print("\n[OK] Pipeline complete.")
    print("  -> evaluation_results.csv")
    print("  -> evaluation_results.json")


if __name__ == "__main__":
    main()
