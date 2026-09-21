SELECT
    product_category,
    product_name,
    SUM(quantity) AS units_sold,
    ROUND(SUM(total_sales), 2) AS revenue
FROM ecommerce_sales
GROUP BY product_category, product_name
ORDER BY revenue DESC
LIMIT 20;
