select
    row_number() over (order by tconst) as title_key,
    tconst,
    primary_title,
    original_title,
    title_type,
    is_adult,
    start_year,
    end_year,
    runtime_minutes,
    genres,
    split_part(genres, ',', 1) as primary_genre,
    average_rating,
    num_votes
from {{ ref('stg_imdb_tv_programs') }}