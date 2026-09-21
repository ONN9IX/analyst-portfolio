-- Olist: категории по выручке
SELECT
    COALESCE(t.product_category_name_english, p.product_category_name, 'unknown') AS category,
    COUNT(DISTINCT oi.order_id) AS orders,
    SUM(oi.order_item_id * 0 + 1) AS items,
    ROUND(SUM(oi.price)::numeric, 2) AS revenue
FROM olist_order_items oi
JOIN olist_orders o USING (order_id)
JOIN olist_products p USING (product_id)
LEFT JOIN product_category_name_translation t USING (product_category_name)
WHERE o.order_status = 'delivered'
GROUP BY 1
ORDER BY revenue DESC;
