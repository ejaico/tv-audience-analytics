from pathlib import Path
import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DATABASE_DIR = PROJECT_ROOT / "warehouse"
DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DATABASE_FILE = DATABASE_DIR / "tv_audience.duckdb"

conn = duckdb.connect(str(DATABASE_FILE))


# --------------------------------------------------
# Load IMDb programs
# --------------------------------------------------

imdb_file = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "imdb_tv_programs.csv"
)

conn.execute(
    """
    CREATE OR REPLACE TABLE imdb_tv_programs_raw AS
    SELECT *
    FROM read_csv_auto(?)
    """,
    [str(imdb_file)],
)


# --------------------------------------------------
# Load public TV viewing
# --------------------------------------------------

public_tv_file = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "public_tv"
    / "public_tv_viewing.csv"
)

conn.execute(
    """
    CREATE OR REPLACE TABLE public_tv_viewing_raw AS
    SELECT *
    FROM read_csv_auto(?)
    """,
    [str(public_tv_file)],
)


# --------------------------------------------------
# Load synthetic viewing
# --------------------------------------------------

synthetic_file = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "synthetic"
    / "synthetic_audience_viewing.csv"
)

conn.execute(
    """
    CREATE OR REPLACE TABLE synthetic_audience_viewing_raw AS
    SELECT *
    FROM read_csv_auto(?)
    """,
    [str(synthetic_file)],
)


# --------------------------------------------------
# Display tables
# --------------------------------------------------

tables = conn.execute(
    "SHOW TABLES"
).fetchall()

print("Tables loaded:")

for table in tables:
    print(table[0])


conn.close()

print()
print(f"DuckDB database created at:")
print(DATABASE_FILE)