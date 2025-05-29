import json, math
from pathlib import Path
from tqdm import tqdm
from agent.agent import agent

DATASET_PATH = Path("tasks/gaia_level1_val.json")
MAX_ITER = 6
NUM_TOL_PCT = 0.01      # 1 % относительная погрешность
NUM_TOL_ABS = 0.01      # 0.01 абс. погрешность

def equal(a, b) -> bool:
    try:
        fa, fb = float(a), float(b)
        return math.isclose(fa, fb, rel_tol=NUM_TOL_PCT, abs_tol=NUM_TOL_ABS)
    except (ValueError, TypeError):
        pass
    return str(a).strip().lower() == str(b).strip().lower()

tasks = json.loads(Path(DATASET_PATH).read_text(encoding="utf-8"))
total = len(tasks)
correct, tokens = 0, 0

for t in tqdm(tasks, desc="GAIA"):
    q, gold = t["question"], t["answer"]
    res = agent.run(q)
    pred = res["answer"] if isinstance(res, dict) else res
    if isinstance(res, dict):
        tokens += res.get("usage", {}).get("total_tokens", 0)
    if equal(pred, gold):
        correct += 1

acc = correct / total * 100
print(f"\nEvaluated {total} tasks")
print(f"Correct  {correct}")
print(f"Accuracy {acc:.1f}%")
if tokens:
    print(f"Tokens   {tokens:,}")