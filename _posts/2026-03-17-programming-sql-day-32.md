---
title: "Programming SQL Practice – Day 32"
date: 2026-03-17
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

### 10 Visa SQL Interview Questions
https://datalemur.com/blog/visa-sql-interview-questions

---
### SQL Interview Question 1: ApplePay Volume
```sql
SELECT 
    merchant_id,
    SUM(
        CASE 
            WHEN LOWER(payment_method) = 'apple pay' 
            THEN transaction_amount
            ELSE 0
        END
    ) AS total_transaction
FROM transactions
GROUP BY merchant_id
ORDER BY total_transaction DESC;
```
**Key Point**
- had to change the payment_method to lower case

### SQL Question 2: Monthly Merchant Balance
```sql
WITH typed AS (
    SELECT
        DATE(transaction_date) AS transaction_date,
        CASE
            WHEN type = 'deposit' THEN amount
            ELSE -amount
        END AS signed_amount
    FROM transactions
),
daily_balance AS (
    SELECT
        transaction_date,
        SUM(signed_amount) AS daily_balance
    FROM typed
    GROUP BY transaction_date
)
SELECT
    transaction_date,
    SUM(daily_balance) OVER (
        PARTITION BY YEAR(transaction_date), MONTH(transaction_date)
        ORDER BY transaction_date
    ) AS cumulative_balance
FROM daily_balance
ORDER BY transaction_date;
```

