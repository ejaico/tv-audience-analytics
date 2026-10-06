select
    viewing_period,
    program_name,
    rank,
    platform_type,
    network_or_provider,
    viewers_000s,
    minutes_viewed_millions,
    household_rating,
    number_of_episodes,
    source_name,
    source_url
from {{ source('raw', 'public_tv_viewing_raw') }}