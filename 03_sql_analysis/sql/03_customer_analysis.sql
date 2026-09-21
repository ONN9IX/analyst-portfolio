SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(oi.total_amount), 2) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
GROUP BY o.customer_id
ORDER BY revenue DESC
LIMIT 20;
