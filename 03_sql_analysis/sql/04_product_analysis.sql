SELECT
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS units_sold,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p USING (product_id)
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;
