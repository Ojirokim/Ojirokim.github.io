---
title: "Programming SQL Practice – Day 25"
date: 2026-02-03
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## 문제 4 — “그로스 팀 요청: 재구매 고객 비율(Repeat Rate)”
**난이도: MEDIUM | 제한시간: 20분**
```sql
with counting as(
select distinct customer_id, count(*)over(partition by customer_id) cnt
from orders
where status = "PAID"
and date(order_datetime) >= '2025-01-01'
and date(order_datetime) <'2026-01-01'
)
select
(select count(customer_id) from counting where cnt>=1) base_customer_cnt,
(select count(customer_id) from counting where cnt>=2) repeat_customer_cnt,
(select count(customer_id) from counting where cnt>=2)/(select count(customer_id) from counting where cnt>=1)*100 repeat_rate_pct;
```
**Key Point**
- Used CTE to get the table with the number of orders for each customer


## 문제 5 — “신규 고객 30일 LTV: 첫 결제일 기준 30일 합 & 30일 내 재구매”
**난이도: HARD | 제한시간: 40분**
```sql
with rownum as(
select
customer_id, order_datetime, amount, ROW_NUMBER()OVER(PARTITION BY customer_id order by order_datetime) rn,
datediff(order_datetime,
FIRST_VALUE(order_datetime)OVER(partition by CUSTOMER_ID order by order_datetime ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)) diff,
sum(amount)over(partition by customer_id order by order_datetime) sm
from orders o
join payments p
on o.order_id = p.order_id 
)
select customer_id, min(order_datetime)over(partition by customer_id
order_datetime, rn, count(*)over(partition by customer_id)
from rownum
where diff<=30
and 
```
**Key Point**
- Did not manage to finish this problem today.
- Will try again tomorrow.