# Cookie Cats dataset

Ожидаемый файл: `cookie_cats.csv`.

Проверенная публичная копия:
`https://raw.githubusercontent.com/ryanschaub/Mobile-Games-A-B-Testing-with-Cookie-Cats/master/cookie_cats.csv`

Каноническое описание набора доступно на Kaggle: **Mobile Games A/B Testing — Cookie Cats**. Набор происходит из учебного проекта DataCamp.

Проверенная схема:
`userid, version, sum_gamerounds, retention_1, retention_7`

Контроль:
- rows: 90 189;
- gate_30: 44 700;
- gate_40: 45 489;
- уникальный userid;
- без пропусков в пяти полях.

Для воспроизводимой загрузки из корня Project 02:
```bash
python download_data.py
```
