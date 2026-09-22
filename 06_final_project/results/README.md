# Проверенные результаты

Эти компактные result-файлы фиксируют ключевые агрегаты, рассчитанные из `data/global_ecommerce_sales.csv`.

- `kpi_summary.csv` — общие KPI;
- `category_performance.csv` — категории;
- `region_performance.csv` — регионы.

Полный `analysis.py` при запуске также генерирует monthly и customer-level выгрузки. Они не коммитятся как обязательные артефакты, чтобы не дублировать производные таблицы без необходимости.

Контрольный Repeat Customer Rate по `Customer_Name`: **25,55%**. Интерпретация ограничена отсутствием стабильного Customer_ID.
