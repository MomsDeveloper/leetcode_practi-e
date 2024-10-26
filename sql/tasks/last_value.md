### Задача 1
Дана таблица `transactions`, необходимо написать запрос, который выводит все значения с дополнительным столбцом `last_amount`, который содержит последнее значение столбца `amount` для каждого `use_id`.

Table: 
```sql
CREATE TABLE transactions (
    use_id INT,
    amount INT,
    dt DATE
);

INSERT INTO transactions (use_id, amount, dt) VALUES
(1, 30, '2024-01-10'),
(1, 20, '2024-01-11'),
(1, 90, '2024-01-12'),
(1, 87, '2024-01-13'),
(1, 10, '2024-01-14'),
(2, 13, '2024-01-10'),
(2, 20, '2024-01-11'),
(2, 100, '2024-01-12');
```

Query:

```sql
select use_id, amount, dt, 
last_value(amount) over w as last_amount
from transactions
window w as (
 partition by use_id 
   rows between unbounded preceding and unbounded following
);
```

### Задача 2
Дана таблица `transactions2`, необходимо оставитиь последнее состояние к 1 сентября

Table: 
```sql
CREATE TABLE transactions2 (
    use_id INT,
    amount INT,
    dt DATE
);
INSERT INTO transactions2 (use_id, amount, dt) VALUES
(1, 30, '2024-01-10'),
(1, 20, '2024-01-27'),
(1, 90, '2024-03-07'),
(1, 87, '2024-06-14'),
(1, 10, '2024-09-14'),
(2, 13, '2024-01-10'),
(2, 20, '2024-05-10'),
(2, 100, '2024-10-17');
```

Query:

```sql
WITH lead_dates AS (
    SELECT 
        use_id,
        amount,
        dt,
        LEAD(dt) OVER (PARTITION BY use_id ORDER BY dt) AS next_dt
    FROM 
        transactions2
)
SELECT 
    use_id,
    amount,
    dt
 from 
 	lead_dates
 where 
    strftime('%m', next_dt) >= '09' 
    AND strftime('%m', dt) <> '09' 
    AND strftime('%m', dt) < '09';
```

