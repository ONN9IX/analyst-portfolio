-- Базовые KPI
SELECT COUNT(DISTINCT order_id) AS orders FROM orders;
SELECT COUNT(DISTINCT customer_id) AS customers FROM orders;
SELECT ROUND(SUM(total_amount), 2) AS revenue FROM order_items;

SELECT ROUND(
    SUM(oi.total_amount) / NULLIF(COUNT(DISTINCT o.order_id), 0), 2
) AS average_order_value
FROM orders o
JOIN order_items oi USING (order_id);
