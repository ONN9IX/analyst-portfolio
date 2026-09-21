# SQL-анализ E-commerce 2023–2024

## Цель
Практический SQL-кейс на современной e-commerce модели: продажи, клиенты, товары, категории, возвраты и динамика бизнеса.

## Требование к данным
В портфолио используются транзакции **не старше 2023 года**. Старый Olist (2016–2018) исключён из проекта.

Целевая схема:
- `customers(customer_id, customer_name, city, state, signup_date)`
- `products(product_id, product_name, category, subcategory, brand, unit_price, cost_price)`
- `orders(order_id, customer_id, order_date, shipping_date, order_status, payment_method, shipping_city)`
- `order_items(order_id, product_id, quantity, unit_price, discount, total_amount)`

## Бизнес-вопросы
- Общая выручка, количество заказов и AOV.
- Динамика продаж по месяцам.
- Повторные покупки и наиболее ценные клиенты.
- Топ товаров и категорий.
- Маржинальность при наличии себестоимости.
- MoM growth и накопительная выручка.

## SQL-навыки
`JOIN`, `GROUP BY`, `CASE`, `CTE`, подзапросы, `LAG`, `RANK`, оконные функции и работа с датами.

## Структура
```text
03_sql_analysis/
├── README.md
├── data/
│   └── README.md
└── sql/
    ├── 01_basic_analysis.sql
    ├── 02_sales_analysis.sql
    ├── 03_customer_analysis.sql
    ├── 04_product_analysis.sql
    ├── 05_cte.sql
    └── 06_window_functions.sql
```

## Принцип
Расчёты строятся из исходных транзакций. Готовые KPI не подставляются вручную.
