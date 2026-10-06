with viewing as (

    select *
    from {{ ref('stg_synthetic_viewing') }}

),

titles as (

    select
        title_key,
        tconst
    from {{ ref('dim_title') }}

),

audiences as (

    select
        audience_key,
        age_band,
        gender,
        income_band
    from {{ ref('dim_audience') }}

),

platforms as (

    select
        platform_key,
        platform_type
    from {{ ref('dim_platform') }}

),

markets as (

    select
        market_key,
        market
    from {{ ref('dim_market') }}

),

campaigns as (

    select
        campaign_key,
        campaign_id
    from {{ ref('dim_campaign') }}

)

select
    viewing.session_id,
    viewing.household_id,
    viewing.viewing_date,

    titles.title_key,
    audiences.audience_key,
    platforms.platform_key,
    markets.market_key,
    campaigns.campaign_key,

    viewing.viewing_minutes,
    viewing.device_type,
    viewing.ad_exposed

from viewing

left join titles
    on viewing.tconst = titles.tconst

left join audiences
    on viewing.age_band = audiences.age_band
    and viewing.gender = audiences.gender
    and viewing.income_band = audiences.income_band

left join platforms
    on viewing.platform_type = platforms.platform_type

left join markets
    on viewing.market = markets.market

left join campaigns
    on viewing.campaign_id = campaigns.campaign_id