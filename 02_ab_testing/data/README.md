# Cookie Cats dataset

Ожидаемый файл: `cookie_cats.csv`.

Проверенная публичная копия:
`https://raw.githubusercontent.com/yufung/ab-testing-cookie-cats/master/data/cookie_cats.csv`

Каноническое описание: Kaggle / DataCamp **Mobile Games A/B Testing — Cookie Cats**.

Проверенная схема:
`userid, version, sum_gamerounds, retention_1, retention_7`

Контроль:
- rows: 90 189;
- gate_30: 44 700;
- gate_40: 45 489;
- Day-1 retained: 20 034 / 20 119;
- Day-7 retained: 8 502 / 8 279;
- уникальный userid;
- без пропусков в пяти полях.

Для воспроизводимой загрузки:
```bash
python download_data.py
```
