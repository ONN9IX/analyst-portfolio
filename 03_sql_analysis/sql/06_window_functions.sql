WITH monthly AS (
    SELECT
        DATE_TRUNC('month', order_date)::date AS month,
        SUM(total_sales) AS revenue
    FROM ecommerce_sales
    GROUP BY 1
),
x AS (
    SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue
    FROM monthly
)
SELECT
    month,
    ROUND(revenue, 2) AS revenue,
    ROUND(100.0 * (revenue - prev_revenue) / NULLIF(prev_revenue, 0), 2) AS mom_growth_pct,
    ROUND(SUM(revenue) OVER (ORDER BY month), 2) AS cumulative_revenue
FROM x
ORDER BY month;
