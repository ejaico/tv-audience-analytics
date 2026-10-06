select
    tconst,
    titleType as title_type,
    primaryTitle as primary_title,
    originalTitle as original_title,
    isAdult as is_adult,
    startYear as start_year,
    endYear as end_year,
    runtimeMinutes as runtime_minutes,
    genres,
    averageRating as average_rating,
    numVotes as num_votes
from {{ source('raw', 'imdb_tv_programs_raw') }}