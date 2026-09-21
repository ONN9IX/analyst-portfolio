SELECT
    DATE_TRUNC('month', o.order_date)::date AS month,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.quantity * oi.price) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
GROUP BY 1
ORDER BY 1;
