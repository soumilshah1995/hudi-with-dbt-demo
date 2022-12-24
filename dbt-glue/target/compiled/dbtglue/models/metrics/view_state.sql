




with cleansed_order as (
    SELECT state,
            count(*) as total_invoice
    FROM hudidb.cleansed_order
    GROUP BY state
    ORDER BY state asc
)

select
    *
from cleansed_order