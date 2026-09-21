SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(SUM(oi.total_amount), 2) AS revenue
FROM order_items oi
JOIN products p USING (product_id)
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 20;
