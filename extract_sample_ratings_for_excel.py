import pandas as pd
from pathlib import Path

# Input compressed IMDb file
input_file = Path("data/raw/imdb/title.ratings.tsv.gz")

# Output folder and file
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "imdb_ratings_sample_50000.csv"

print("Reading the first 50,000 rows...")

sample = pd.read_csv(
    input_file,
    sep="\t",
    nrows=50_000,
    na_values="\\N"
)

print("Rows extracted:", len(sample))
print("Columns found:", len(sample.columns))

sample.to_csv(
    output_file,
    index=False
)

print(f"Saved file to: {output_file}")