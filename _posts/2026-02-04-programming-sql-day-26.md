---
title: "Programming SQL Practice – Day 26"
date: 2026-02-04
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## 문제 5 — “신규 고객 30일 LTV: 첫 결제일 기준 30일 합 & 30일 내 재구매”
**난이도: HARD | 제한시간: 40분**
```sql
with rownum as(
select
customer_id, o.order_datetime, paid_at , amount, FIRST_VALUE(p.paid_at)OVER(partition by CUSTOMER_ID order by p.paid_at ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) first_day
from orders o
join payments p
on o.order_id = p.order_id
where o.status = "PAID"
)
select customer_id, date(first_day) first_paid_date, sum(amount) ltv_30d,
case when count(*)>=2 then 1 else 0 end has_repeat_30d
from rownum
where paid_at< (first_day + interval 30 day)
group by customer_id, first_day
order by ltv_30d desc, customer_id;
```
**Key Point**
- Window function to calculate the first value of a column in a partition.
- used interval to calculate the date.