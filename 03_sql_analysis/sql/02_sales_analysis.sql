-- Olist: месячная динамика продаж
SELECT
    DATE_TRUNC('month', o.order_purchase_timestamp)::date AS month,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(SUM(oi.price)::numeric, 2) AS product_revenue,
    ROUND(AVG(oi.price)::numeric, 2) AS avg_item_price
FROM olist_orders o
JOIN olist_order_items oi USING (order_id)
WHERE o.order_status = 'delivered'
GROUP BY 1
ORDER BY 1;
