SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS orders,
    SUM(oi.quantity * oi.price) AS revenue
FROM orders o
JOIN order_items oi USING (order_id)
GROUP BY o.customer_id
ORDER BY revenue DESC;
