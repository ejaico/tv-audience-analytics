from pathlib import Path
import pandas as pd

# Always build paths relative to the project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = PROJECT_ROOT / "data" / "raw" / "imdb"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# 1. Read IMDb title data
# --------------------------------------------------

print("Reading IMDb title data...")

titles = pd.read_csv(
    INPUT_DIR / "title.basics.tsv.gz",
    sep="\t",
    na_values="\\N",
    dtype="string"
)

print("IMDb columns found:")
print(titles.columns.tolist())

# Convert numeric fields after loading the file
titles["startYear"] = pd.to_numeric(
    titles["startYear"],
    errors="coerce"
)

titles["runtimeMinutes"] = pd.to_numeric(
    titles["runtimeMinutes"],
    errors="coerce"
)

# --------------------------------------------------
# 2. Keep television programs
# --------------------------------------------------

print("Filtering television programs...")

tv_titles = titles[
    titles["titleType"].isin(["tvSeries", "tvMiniSeries"])
].copy()

# Keep titles from 2010 onward
tv_titles = tv_titles[
    tv_titles["startYear"].between(2010, 2025)
].copy()

# --------------------------------------------------
# 3. Read IMDb ratings
# --------------------------------------------------

print("Reading IMDb ratings...")

ratings = pd.read_csv(
    INPUT_DIR / "title.ratings.tsv.gz",
    sep="\t",
    na_values="\\N",
    dtype="string"
)

ratings["averageRating"] = pd.to_numeric(
    ratings["averageRating"],
    errors="coerce"
)

ratings["numVotes"] = pd.to_numeric(
    ratings["numVotes"],
    errors="coerce"
)

# --------------------------------------------------
# 4. Combine title information and ratings
# --------------------------------------------------

print("Combining title data and ratings...")

tv_programs = tv_titles.merge(
    ratings,
    on="tconst",
    how="left"
)

# Rank by number of votes and retain the top 1,500 programs
tv_programs = tv_programs.sort_values(
    by="numVotes",
    ascending=False
).head(1500)

# --------------------------------------------------
# 5. Save the processed file
# --------------------------------------------------

output_file = OUTPUT_DIR / "imdb_tv_programs.csv"

tv_programs.to_csv(
    output_file,
    index=False
)

print(f"Finished. Saved file to: {output_file}")
print(f"Rows saved: {len(tv_programs):,}")