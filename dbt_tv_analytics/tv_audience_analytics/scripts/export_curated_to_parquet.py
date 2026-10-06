from pathlib import Path
import duckdb


PROJECT_ROOT = Path(__file__).resolve().parents[3]

DB_PATH = PROJECT_ROOT / "warehouse" / "tv_audience.duckdb"
OUTPUT_DIR = PROJECT_ROOT / "data" / "exports" / "parquet"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


conn = duckdb.connect(str(DB_PATH))


tables = [
    "dim_title",
    "dim_audience",
    "dim_date",
    "dim_platform",
    "dim_market",
    "dim_campaign",
    "fact_viewing_session",
    "fact_public_viewing",
]


for table in tables:

    output_file = OUTPUT_DIR / f"{table}.parquet"

    print(f"Exporting {table}...")

    conn.execute(
        f"""
        COPY main.{table}
        TO '{output_file}'
        (FORMAT PARQUET)
        """
    )

    print(f"Saved: {output_file}")


conn.close()

print("Finished exporting curated data.")
