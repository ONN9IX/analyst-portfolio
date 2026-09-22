# QA / проверка портфолио

Дата полной повторной проверки: 2026-09-22.

## Данные и расчёты
- [x] Project 01 и Project 06 используют идентичный `global_ecommerce_sales.csv`;
- [x] 2 000 строк, 2 000 уникальных Order_ID, период 2023-01-02 — 2025-12-31;
- [x] Revenue = 484 559,34;
- [x] Profit = 158 872,32;
- [x] Orders = 2 000;
- [x] Customers = 1 534;
- [x] Units = 7 115;
- [x] AOV = 242,28;
- [x] Profit Margin = 32,79%;
- [x] Shipping Cost = 25 804,24;
- [x] Repeat Customer Rate по Customer_Name = 25,55%;
- [x] формула Total_Sales сверена с Quantity × Unit_Price × (1 − Discount_Percent/100) с учётом округления;
- [x] category/region result-файлы согласованы со схемой `analysis.py`.

## A/B Testing
- [x] публичный источник Cookie Cats доступен;
- [x] downloader исправлен на рабочий raw GitHub path;
- [x] 90 189 пользователей: gate_30 = 44 700, gate_40 = 45 489;
- [x] Day-1 retained = 20 034 / 20 119;
- [x] Day-7 retained = 8 502 / 8 279;
- [x] Day-1: 44,82% vs 44,23%, p = 0,0755;
- [x] Day-7: 19,02% vs 18,20%, p = 0,0016;
- [x] выводы README соответствуют двустороннему chi-square test при α=0,05.

## SQL
- [x] Revenue во всех запросах использует `total_sales`;
- [x] README больше не заявляет ошибочную формулу Quantity × Unit_Price;
- [x] CTE, подзапрос и оконные функции действительно присутствуют;
- [x] JOIN не заявляется, поскольку в проекте одна плоская таблица.

## Marketing
- [x] 1 000 строк, 2024-01-01 — 2024-01-30;
- [x] Impressions = 10 785 810;
- [x] Clicks = 1 027 999;
- [x] CTR = 9,53%;
- [x] Acquisition Cost = 12 283 827,89;
- [x] CPC = 11,95;
- [x] cost-weighted ROI = 4,97;
- [x] click-weighted Conversion Rate = 8,04%;
- [x] synthetic/educational происхождение указано явно.

## BI и документация
- [x] Project 05 описывает фактически собранный Yandex DataLens dashboard;
- [x] DataLens calculated fields совпадают с проверенными KPI;
- [x] устаревшие Power BI/DAX материалы удалены;
- [x] Final Project spec больше не содержит Power BI;
- [x] корневой README не заявляет отсутствующие JOIN/Matplotlib;
- [x] ветка переработки успешно merged в `main`.

## Автоматизация
GitHub Actions workflow `Portfolio QA` добавлен для compile и запуска Python-проектов. На момент этой проверки GitHub API не показывает выполненных workflow runs, поэтому факт успешного CI-запуска не заявляется.

## Принцип
В портфолио не заявляются результаты, которые не подтверждены исходными данными, воспроизводимым расчётом или фактически собранным артефактом.
