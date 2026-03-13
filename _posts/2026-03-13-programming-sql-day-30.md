---
title: "Programming SQL Practice – Day 30"
date: 2026-03-13
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## [금융] SQL 코딩 테스트

---
## 문제 4 — “대출 리스크 리포트: 2025-12 연체 고객 비율(세그먼트별)”
**난이도: HARD | 제한시간: 40분**
```sql
select segment, count(*) due_customer_cnt,
count(missed) delinquent_customer_cnt,
count(missed)/count(*) *100 delinquency_rate_pct
from 
(select distinct l.customer_id, segment,
max(case when lp.status='MISSED' then 1 end) missed
from loans l
join customers c
on l.customer_id = c.customer_id
join loan_payments lp 
on l.loan_id = lp.loan_id 
where lp.due_date >= '2025-12-01' and lp.due_date < '2026-01-01'
and l.status IN ('ACTIVE','DEFAULT')
group by customer_id , segment) A
group by SEGMENT
order by delinquency_rate_pct desc, due_customer_cnt desc, segment
```

