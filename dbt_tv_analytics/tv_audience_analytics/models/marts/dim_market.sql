
with mark as (
        select distinct
        market
    from {{ ref('stg_synthetic_viewing') }}
)
select row_number() over (order by market) as market_key
,market
from mark