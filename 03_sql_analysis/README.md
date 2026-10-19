# SQL-анализ Global E-Commerce 2023–2025

SQL-запросы к тому же **учебному** CSV, что в проекте 01. Анализ показывает, как получать бизнес-показатели средствами PostgreSQL.

## Dataset
`global_ecommerce_sales.csv`: 2 000 заказов, период 2023–2025. Revenue берётся из исходного поля `total_sales`, которое уже учитывает скидку.

## Что демонстрирует
- DDL, типы данных и ограничения качества;
- агрегаты и GROUP BY;
- CTE;
- подзапрос;
- LAG;
- cumulative SUM;
- MoM growth;
- анализ клиентов, товаров и категорий.

## Файлы
- `00_schema.sql` — таблица и ограничения;
- `01_basic_analysis.sql` — основные KPI;
- `02_sales_analysis.sql` — месячная динамика;
- `03_customer_analysis.sql` — клиенты;
- `04_product_analysis.sql` — товары;
- `05_cte.sql` — CTE + подзапрос;
- `06_window_functions.sql` — LAG, MoM и cumulative revenue.

## Как воспроизвести

Из корня репозитория перейдите в эту папку и выполните команды в `psql`:

```bash
cd 03_sql_analysis
psql -d your_database -f sql/00_schema.sql
```

Затем в интерактивном `psql` (после `cd 03_sql_analysis`):

```sql
\copy ecommerce_sales FROM '../01_sales_analysis/data/global_ecommerce_sales.csv' WITH (FORMAT csv, HEADER true)
\i sql/01_basic_analysis.sql
\i sql/02_sales_analysis.sql
```

Остальные SQL-файлы из папки `sql/` запускаются аналогично. Пути в примере предполагают запуск из `03_sql_analysis/`. Для копирования CSV требуется локальный доступ к файлу.

## Ограничение

В исходном CSV одна строка соответствует одному заказу; таблица хранится без разбиения на связанные сущности. JOIN показаны отдельно в [Relational SQL Case](../07_relational_sql_case/).
