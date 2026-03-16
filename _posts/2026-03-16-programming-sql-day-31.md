---
title: "Programming SQL Practice – Day 31"
date: 2026-03-16
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## [금융] SQL 코딩 테스트

---
## 문제 5 — “AML 이상출금 탐지: ‘30일 평균 대비 3배 이상 급증’ 날짜 찾기”
**난이도: HARD | 제한시간: 50분 OVER.. HELL**
```sql
WITH withdrawals AS (
    SELECT
        a.customer_id,
        DATE(t.tx_time) AS dt,
        SUM(-t.amount * fx.rate) AS withdraw_usd
    FROM transactions t
    JOIN accounts a
        ON t.account_id = a.account_id
    JOIN fx_rates fx
        ON fx.rate_date = DATE(t.tx_time)
       AND fx.from_currency = t.currency
       AND fx.to_currency = 'USD'
    WHERE t.tx_type = 'WITHDRAWAL'
      AND t.status = 'SETTLED'
    GROUP BY a.customer_id, DATE(t.tx_time)
),
customer_days AS (
    SELECT
        c.customer_id,
        d.date AS dt
    FROM customers c
    CROSS JOIN calendar_dates d
),
daily AS (
    SELECT
        cd.customer_id,
        cd.dt,
        COALESCE(w.withdraw_usd, 0) AS withdraw_usd
    FROM customer_days cd
    LEFT JOIN withdrawals w
      ON cd.customer_id = w.customer_id
     AND cd.dt = w.dt
),
scored AS (
    SELECT
        customer_id,
        dt,
        withdraw_usd,
        AVG(withdraw_usd) OVER (
            PARTITION BY customer_id
            ORDER BY dt
            ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING
        ) AS avg_prev30_usd
    FROM daily
)
SELECT
    customer_id,
    dt AS date,
    withdraw_usd,
    avg_prev30_usd,
    withdraw_usd / avg_prev30_usd AS spike_multiple
FROM scored
WHERE avg_prev30_usd IS NOT NULL
  AND withdraw_usd >= 1000
  AND withdraw_usd >= 3 * avg_prev30_usd
ORDER BY spike_multiple DESC, withdraw_usd DESC, customer_id ASC, date ASC
LIMIT 100;
```

