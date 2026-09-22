# A/B-тест Cookie Cats: влияние положения gate на retention

## Бизнес-задача
В Cookie Cats проверялось изменение первого progression gate с уровня 30 на уровень 40.

- **Control:** `gate_30`
- **Treatment:** `gate_40`
- **H0:** retention одинаков в двух группах.
- **H1:** retention различается.
- Уровень значимости: **α = 0.05**.

## Данные
Публичный Cookie Cats A/B dataset: **90 189 игроков**, 5 полей:
`userid`, `version`, `sum_gamerounds`, `retention_1`, `retention_7`.

Источник: Kaggle / DataCamp Cookie Cats dataset. В `data/README.md` зафиксированы проверенные ссылки. Сам CSV не дублируется в репозитории; `download_data.py` скачивает точную публичную копию.

## Проверенные результаты

| Метрика | gate_30 | gate_40 | Разница gate_40 − gate_30 | p-value | 95% CI для gate_40 − gate_30 |
|---|---:|---:|---:|---:|---:|
| Users | 44 700 | 45 489 | — | — | — |
| Day-1 retention | 44,82% | 44,23% | -0,59 п.п. | 0,0755 | [-1,24; 0,06] п.п. |
| Day-7 retention | 19,02% | 18,20% | -0,82 п.п. | 0,0016 | [-1,33; -0,31] п.п. |

Retained users:
- Day 1: gate_30 = **20 034**, gate_40 = **20 119**;
- Day 7: gate_30 = **8 502**, gate_40 = **8 279**.

## Интерпретация
На Day 1 наблюдаемая разница мала и при α=0,05 статистически незначима.

На Day 7 перенос gate с уровня 30 на 40 связан со снижением retention примерно на **0,82 п.п.**; двусторонний chi-square test даёт **p ≈ 0,0016**, а 95% CI разницы не включает ноль. В рамках этого эксперимента данные не поддерживают перенос gate на уровень 40, если целевая метрика — Day-7 retention.

Это вывод по retention, а не оценка финансового эффекта: в наборе нет revenue, purchases или стоимости изменения продукта.

## Методология
1. Проверка схемы, пропусков, дубликатов userid и экспериментальных групп.
2. Retention rate и абсолютная разница долей.
3. Chi-square test для бинарных метрик.
4. 95% Wald CI для разницы долей.
5. Bootstrap CI как дополнительная проверка устойчивости.
6. Отдельный descriptive-анализ `sum_gamerounds`; экстремальный выброс делает среднее чувствительным.

## Запуск
```bash
pip install -r requirements.txt
python download_data.py
python analysis.py
```

`analysis.py` также подскажет запустить загрузчик, если CSV отсутствует.

## Структура
```text
02_ab_testing/
├── README.md
├── analysis.py
├── download_data.py
├── requirements.txt
├── data/
│   └── README.md
├── sql/
│   └── ab_analysis.sql
└── results/
    └── retention_results.csv
```

## Навыки
A/B testing, Pandas, NumPy, SciPy, Statsmodels, hypothesis testing, confidence intervals, bootstrap, SQL.
