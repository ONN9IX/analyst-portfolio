WITH monthly AS (
    SELECT
        DATE_TRUNC('month', o.order_date)::date AS month,
        SUM(oi.quantity * oi.price) AS revenue
    FROM orders o
    JOIN order_items oi USING (order_id)
    GROUP BY 1
)
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS previous_month_revenue,
    ROUND(
        100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
        / NULLIF(LAG(revenue) OVER (ORDER BY month), 0),
        2
    ) AS mom_growth_pct,
    SUM(revenue) OVER (ORDER BY month) AS cumulative_revenue
FROM monthly
ORDER BY month;
