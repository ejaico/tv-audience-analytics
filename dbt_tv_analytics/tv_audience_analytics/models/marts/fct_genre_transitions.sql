with viewing_sequence as (
    select
        household_id,
        viewing_date,
        viewing_sequence,
        primary_genre
    from {{ ref('stg_synthetic_viewing') }}
),

genre_with_previous as (
    select
        household_id,
        viewing_date,
        viewing_sequence,
        primary_genre as current_genre,
        lag(primary_genre) over (
            partition by household_id
            order by viewing_sequence
        ) as previous_genre
    from viewing_sequence
),

transition_counts as (
    select
        previous_genre,
        current_genre,
        count(*) as transition_count

    from genre_with_previous
    where previous_genre is not null
    group by
        previous_genre,
        current_genre
)

select
    previous_genre,
    current_genre,
    transition_count,
    round(
        transition_count * 100.0
        / sum(transition_count) over (partition by previous_genre),2
        ) as transition_pct

from transition_counts
order by
    previous_genre,
    transition_count desc