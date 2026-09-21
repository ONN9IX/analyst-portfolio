# Power BI Dashboard — спецификация

## Данные
Только период **2023+**.

## Page 1 — Overview
KPI: Revenue, Orders, Customers, AOV, Profit, Profit Margin. Линейный график Revenue by Month. Slicers: Date, Region, Category.

## Page 2 — Sales
Revenue by Month, Orders by Month, Revenue by Category, Revenue by Region.

## Page 3 — Products
Top products by Revenue, Profit by Product, Category performance.

## Page 4 — Customers
Revenue by customer segment, customer count, repeat customers при наличии истории заказов.

## Требования
- единый Date table;
- связи many-to-one;
- меры из `measures.dax`;
- никаких вручную введённых KPI;
- screenshots страниц после сборки .pbix.
