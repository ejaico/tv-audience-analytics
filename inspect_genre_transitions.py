import duckdb

DB_PATH = "warehouse/tv_audience.duckdb"

con = duckdb.connect(DB_PATH)

query = """
select
    previous_genre,
    current_genre,
    transition_count,
    transition_pct
from fct_genre_transitions
order by previous_genre, transition_count desc
"""

result = con.execute(query).fetchdf()

print(result)

con.close()