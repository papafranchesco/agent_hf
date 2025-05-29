from datasets import load_dataset
import random, json, pathlib

ds = load_dataset(
    "gaia-benchmark/GAIA",
    "2023_level1",
    split="validation",      # валидационный сплит содержит ответы
    trust_remote_code=True,
)

subset = random.sample(list(ds), k=len(ds))
pathlib.Path("tasks").mkdir(exist_ok=True)

with open("tasks/gaia_level1_val.json", "w", encoding="utf-8") as f:
    json.dump(
        [
            {
                "question": ex["Question"],
                "answer":   ex["Final answer"],
            }
            for ex in subset
        ],
        f,
        ensure_ascii=False,
        indent=2,
    )

print(f" Saved ({len(subset)} items)")
