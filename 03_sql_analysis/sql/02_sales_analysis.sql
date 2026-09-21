SELECT
    DATE_TRUNC('month', o.order_date)::date AS month,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(oi.total_amount), 2) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
GROUP BY 1
ORDER BY 1;
