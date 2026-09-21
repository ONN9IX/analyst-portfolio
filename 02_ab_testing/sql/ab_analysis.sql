-- Cookie Cats A/B test: exploratory SQL
-- gate_30 = control, gate_40 = treatment

SELECT version, COUNT(*) AS users
FROM cookie_cats
GROUP BY version
ORDER BY version;

SELECT
    version,
    ROUND(AVG(sum_gamerounds), 2) AS avg_game_rounds,
    AVG(CASE WHEN retention_1 THEN 1.0 ELSE 0.0 END) AS retention_1,
    AVG(CASE WHEN retention_7 THEN 1.0 ELSE 0.0 END) AS retention_7
FROM cookie_cats
GROUP BY version
ORDER BY version;

SELECT
    version,
    SUM(CASE WHEN retention_1 THEN 1 ELSE 0 END) AS retained_day_1,
    SUM(CASE WHEN retention_7 THEN 1 ELSE 0 END) AS retained_day_7
FROM cookie_cats
GROUP BY version
ORDER BY version;
