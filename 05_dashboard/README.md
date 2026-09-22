# Yandex DataLens — E-commerce Sales Dashboard

## Цель
Интерактивный BI-дашборд по e-commerce данным за 2023–2025 годы. Проект демонстрирует построение бизнес-KPI, визуализацию динамики продаж и работу с интерактивными фильтрами в Yandex DataLens.

## Источник
Используется тот же файл `global_ecommerce_sales.csv`, что и в Project 01: 2 000 заказов за период 2023-01-02 — 2025-12-31.

## KPI
- Revenue — 484 559,34
- Profit — 158 872,32
- Orders — 2 000
- Customers — 1 534
- Units Sold — 7 115
- AOV — 242,28
- Profit Margin — 32,79%

## Визуализации
- Revenue by Month
- Revenue by Category
- Revenue by Region
- Revenue by Customer Segment
- Profit Margin by Category
- Top Products by Revenue

## Интерактивные селекторы
- Region
- Product Category
- Customer Segment
- Order Date

## Ограничение данных
В источнике отсутствует отдельный Customer_ID, поэтому количество клиентов рассчитывается как COUNTD(Customer_Name). Это допустимо для учебного набора, но в production-модели предпочтителен стабильный уникальный идентификатор клиента.

## Файлы
- `DASHBOARD_SPEC.md` — структура фактически собранного дашборда;
- `CALCULATED_FIELDS.md` — формулы вычисляемых полей DataLens.

Дашборд фактически собран и проверен в Yandex DataLens. KPI сверены с Python-анализом Project 01/06.
