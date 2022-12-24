{{ config(materialized='table') }}

{{ config(
    materialized='incremental',
    file_format='hudi',
    incremental_strategy='merge',
    unique_key='invoice_id',
    options={
        'type': 'cow',
        'primaryKey': 'invoice_id',
        'precombineKey': 'item_id'
    },
   )
}}


with source_data as (
    SELECT
        invoiceid ,
        category ,
        destinationstate,
        itemid
    FROM {{ source('data_source', 'order') }}
)

select
    invoiceid as invoice_id,
    source_data.category as category,
    source_data.destinationstate as state,
    source_data.itemid as item_id
from source_data

