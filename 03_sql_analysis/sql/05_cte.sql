-- Olist: клиенты с выручкой выше средней клиентской выручки
WITH customer_sales AS (
    SELECT
        c.customer_unique_id,
        SUM(oi.price) AS revenue
    FROM olist_customers c
    JOIN olist_orders o USING (customer_id)
    JOIN olist_order_items oi USING (order_id)
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
)
SELECT customer_unique_id, ROUND(revenue::numeric, 2) AS revenue
FROM customer_sales
WHERE revenue > (SELECT AVG(revenue) FROM customer_sales)
ORDER BY revenue DESC;
