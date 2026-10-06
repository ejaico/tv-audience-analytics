select row_number() over (order by age_band, gender, income_band) as audience_key
, age_band
, gender
, income_band

from (
    select distinct age_band
    , gender
    , income_band
    from {{ ref('stg_synthetic_viewing') }}
)