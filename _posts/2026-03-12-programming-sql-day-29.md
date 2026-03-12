---
title: "Programming SQL Practice – Day 29"
date: 2026-03-12
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## [금융] SQL 코딩 테스트

---
## 문제 1 — “카드 승인율 대시보드: 등급별 승인/거절/승인율”
**난이도: EASY  | 제한시간: 20분**
```sql
select card_tier, count(*) attempt_cnt,
sum(case when status='SETTLED' then 1 end) approved_cnt,
round(sum(case when status='SETTLED' then 1 end)/count(*) *100,2) approval_rate_pct
from transactions t
join cards c
on t.account_id = c.account_id 
where tx_time>= '2025-10-01' and tx_time <'2026-01-01'
and tx_type = 'CARD_PURCHASE'
group by c.card_tier
order by 4 desc, 2 desc, 1;
```
**Key Point**
- Using Case when to calculate approval rate and sort by approval rate


## 문제 2 — “수수료 매출 집계: 월별·통화별 수수료 거래 건수/금액”
**난이도: EASY | 제한시간: 15분**
```sql
select DATE_FORMAT(tx_time, '%Y-%m') ym, currency, count(*) fee_tx_cnt, -sum(t.amount)total_fee_amount
from transactions t 
where tx_type = 'FEE'
and status = 'SETTLED'
and tx_time>= '2025-01-01' and tx_time <'2026-01-01'
group by DATE_FORMAT(tx_time, '%Y-%m'), currency
order by 1, 2
```
**Key Point**
- Using DATE_FORMAT to format date and group by month and currency


## 문제 3 — “분기 순자금유입(Net Inflow) TOP 고객: 다통화 USD 환산”
**난이도: MEDIUM | 제한시간: 25분**
```sql
select c.customer_id, segment, country, sum(amount * rate) net_inflow_usd
from transactions t
join accounts a
on t.account_id = a.account_id
join customers c
on a.customer_id = c.customer_id 
join fx_rates f
on DATE(f.rate_date) = DATE(t.tx_time)
and f.from_currency = t.currency
where tx_time>= '2025-10-01' and tx_time <'2026-01-01'
and f.to_currency = 'USD'
and tx_type in ('DEPOSIT', 'WITHDRAWAL', 'TRANSFER_IN','TRANSFER_OUT')
and status='SETTLED'
group by customer_id, segment, country
order by net_inflow_usd desc, customer_id
limit 20;
```
**Key Point**
- used Date function to format date and join two tables using them.