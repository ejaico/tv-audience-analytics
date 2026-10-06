import duckdb

DB_PATH = "warehouse/tv_audience.duckdb"
OUTPUT_PATH = "data/processed/fct_genre_transitions.parquet"

con = duckdb.connect(DB_PATH)

con.execute(f"""
    COPY (
        SELECT *
        FROM fct_genre_transitions
    )
    TO '{OUTPUT_PATH}'
    (FORMAT PARQUET)
""")

con.close()

print(f"Created: {OUTPUT_PATH}")