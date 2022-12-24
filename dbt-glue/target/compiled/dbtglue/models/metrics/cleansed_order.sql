




with source_data as (
    SELECT
        invoiceid ,
        category ,
        destinationstate,
        itemid
    FROM hudidb.order
)

select
    invoiceid as invoice_id,
    source_data.category as category,
    source_data.destinationstate as state,
    source_data.itemid as item_id
from source_data