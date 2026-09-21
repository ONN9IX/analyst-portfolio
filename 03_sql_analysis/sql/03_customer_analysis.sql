-- Olist: повторные покупки считаем по customer_unique_id,
-- так как customer_id в этом датасете привязан к заказу.
WITH customer_orders AS (
    SELECT
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS orders,
        SUM(oi.price) AS revenue
    FROM olist_customers c
    JOIN olist_orders o USING (customer_id)
    JOIN olist_order_items oi USING (order_id)
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
)
SELECT
    customer_unique_id,
    orders,
    ROUND(revenue::numeric, 2) AS revenue
FROM customer_orders
ORDER BY revenue DESC
LIMIT 20;
