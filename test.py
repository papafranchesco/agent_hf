from datasets import load_dataset
ds = load_dataset(
    "gaia-benchmark/GAIA",
    "2023_level1",
    split="validation",
    trust_remote_code=True,
)
print(ds[0])
print(ds.features)
