{{ config(materialized='table') }}

{{ config(
    materialized='incremental',
    file_format='hudi',
    incremental_strategy='merge',
    unique_key='state',
    options={
        'type': 'cow',
        'primaryKey': 'state',
        'precombineKey': 'total_invoice'
    },
   )
}}


with cleansed_order as (
    SELECT state,
            count(*) as total_invoice
    FROM {{ ref('cleansed_order') }}
    GROUP BY state
    ORDER BY state asc
)

select
    *
from cleansed_order


