with camp as (
    select distinct campaign_id
    from {{ref('stg_synthetic_viewing')}}
    where campaign_id is not null
)

select row_number() over (order by campaign_id) as campaign_key
, campaign_id
, case when campaign_id = 'CMP001' then 'Campaign 1'
     when campaign_id = 'CMP002' then 'Campaign 2'
     when campaign_id = 'CMP003' then 'Campaign 3'
end as campaign_name

from camp