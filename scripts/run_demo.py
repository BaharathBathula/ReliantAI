import json
from pathlib import Path

from evaluation.evaluator import evaluate_interaction

INPUT_PATH = Path("demo_data/sample_interactions.jsonl")
OUTPUT_PATH = Path("outputs/evaluated_results.jsonl")

def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with INPUT_PATH.open("r", encoding="utf-8") as fin, OUTPUT_PATH.open("w", encoding="utf-8") as fout:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            event = json.loads(line)
            evaluated = evaluate_interaction(event)
            fout.write(json.dumps(evaluated) + "\n")
            count += 1

    print(f"✅ Evaluated {count} interactions")
    print(f"📄 Output written to: {OUTPUT_PATH}")

    # Print a short summary
    high_risk = 0
    with OUTPUT_PATH.open("r", encoding="utf-8") as fin:
        for line in fin:
            obj = json.loads(line)
            if obj["severity"] in ("high", "critical"):
                high_risk += 1
    print(f"⚠️ High/Critical findings: {high_risk}")

if __name__ == "__main__":
    main()
