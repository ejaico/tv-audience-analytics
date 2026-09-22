import pandas as pd
from pathlib import Path

INPUT_DIR = Path("data/raw/imdb")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("Reading IMDb title data...")

# === Read basics file
titles = pd.read_csv(
    INPUT_DIR / "title.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    dtype={
        "tconst": "string",
        "titleType": "string",
        "primaryTitle": "string",
        "originalTitle": "string",
        "isAdult": "Int64",
        "startYear": "string",
        "endYear": "string",
        "runtimeMinutes": "float",
        "genres": "string"
    }
)

titles["runtimeMinutes"] = pd.to_numeric(
    titles["runtimeMinutes"],
    errors="coerce"
)

print("Filtering TV series...")

tv = titles[
    titles["titleType"].isin(["tvSeries", "tvMiniSeries"])
].copy()

tv["startYear"] = pd.to_numeric(tv["startYear"], errors="coerce")

tv = tv[
    (tv["startYear"] >= 2010) &
    (tv["startYear"] <= 2025)
]

print(f"TV programs found: {len(tv):,}")

# === Read ratings file
ratings = pd.read_csv(
    INPUT_DIR / "title.ratings.tsv.gz",
    sep="\t"
)

# === Join the datasets
tv = tv.merge(
    ratings,
    on="tconst",
    how="left"
)

# === Sort the joined dataset by votes (descending) and only view top 1500 rows
tv = tv.sort_values(
    "numVotes",
    ascending=False
).head(1500)

tv = tv[
    [
        "tconst",
        "primaryTitle",
        "titleType",
        "startYear",
        "endYear",
        "runtimeMinutes",
        "genres",
        "averageRating",
        "numVotes"
    ]
]

output_file = OUTPUT_DIR / "imdb_tv_programs.csv"

tv.to_csv(output_file, index=False)

print(f"Saved: {output_file}")