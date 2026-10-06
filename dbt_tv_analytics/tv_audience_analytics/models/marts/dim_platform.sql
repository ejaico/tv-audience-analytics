select
    row_number() over (
        order by platform_type
    ) as platform_key,
    platform_type
from (
    select distinct
        platform_type
    from {{ ref('stg_synthetic_viewing') }}
)