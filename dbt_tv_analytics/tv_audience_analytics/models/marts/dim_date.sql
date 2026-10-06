with dates as (

    select *
    from generate_series(
        date '2026-01-01',
        date '2026-08-31',
        interval '1 day'
    )

)select
    cast(generate_series as date) as date,
    extract(year from generate_series) as year,
    extract(quarter from generate_series) as quarter,
    extract(month from generate_series) as month,
    strftime(generate_series, '%B') as month_name,
    extract(week from generate_series) as week,
    extract(dow from generate_series) as day_of_week_number,
    strftime(generate_series, '%A') as day_of_week_name

from dates