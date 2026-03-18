---
title: "Programming SQL Practice – Day 33"
date: 2026-03-18
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

### 10 Visa SQL Interview Questions
https://datalemur.com/blog/visa-sql-interview-questions

---
### SQL Question 4: Calculate the Total Number of Transactions and Average Transaction Amount per Country
```sql
WITH monthly_stats AS (
    SELECT
        DATE_TRUNC('month', transaction_date) AS mth,
        country,
        COUNT(transaction_id) AS total_transactions,
        AVG(amount) AS average_amount
    FROM transactions
    GROUP BY mth, country
)
SELECT
     mth,
     country,
     total_transactions,
     average_amount,
     RANK() OVER(PARTITION BY country ORDER BY total_transactions DESC) AS rank
FROM monthly_stats
ORDER BY mth, country;
```
**Key Point**
- used Date_trunc() function to truncate the date to the nearest month

### SQL Question 6: Design Visa's Transaction Database
```sql
Select c.cardholder_id, count(t.transaction_id) as transaction_count, sum(amount) as total_amount
from transaction t
join cardholder c 
on t.card_id = c.cardholder_id
join merchant m 
on t.merchant_id = m.merchant_id
where c.country = m.country
and transaction_date >='2022-07-01' and transaction_date < '2022-8-01'
group by c.cardholder_id
HAVING SUM(t.amount) > 1000
```
**Key Point**
- Joined 3 tables together then filtered by country and date
