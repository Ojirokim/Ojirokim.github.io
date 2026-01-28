---
title: "Programming SQL Practice – Day 20"
date: 2026-01-27
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
A
---

## 문제 1 — “결제 모니터링 대시보드: 주문 상태별 KPI
**난이도: EASY | 제한시간: 15분**
```sql
SELECT
  o.status,
  COUNT(*) AS order_cnt,
  COALESCE(SUM(p.amount), 0) AS total_paid_amount
FROM orders o
LEFT JOIN payments p
  ON o.order_id = p.order_id
WHERE o.order_datetime >= '2025-01-01'
  AND o.order_datetime <  '2026-01-01'
GROUP BY o.status
ORDER BY o.status;
```
**Key Point**
- Used Left join to include the Cancelled orders.
- Used COALESCE to handle null values
- Important to bring refunded amount into the total paid amount calculation


## 문제 2 — “VIP 케어 리스트: 평균 주문금액 TOP 10”
**난이도: EASY | 제한시간: 15분**
```sql
select c.customer_id, count(*) order_cnt, round(avg(amount), 2) avg_order_amount
from orders o	
join customers c
on o.customer_id = c.customer_id 
join payments p
on o.order_id = p.order_id
where c.is_vip = 1
and o.status = 'PAID'
and o.order_datetime between '2025-01-01' and '2025-12-31'
group by c.customer_id 
order by avg_order_amount desc, order_cnt desc, customer_id
limit 10
```
**Key Point**
- Used join to get the customer_id and order_cnt
- Used group by to get the avg_order_amount
- Important to do round() for the avg_order_amount


## 문제 3 — “상품기획 손익 리포트: 카테고리별 매출/GP/마진율”
**난이도: MEDIUM | 제한시간: 25분**
```sql
select category, SUM(oi.item_price * oi.quantity - oi.discount_amount) revenue, 
SUM(oi.item_price * oi.quantity - oi.discount_amount) - sum(p.unit_cost* oi.quantity) grss_profit,
case when SUM(oi.item_price * oi.quantity - oi.discount_amount) = 0 then null
else (SUM(oi.item_price * oi.quantity - oi.discount_amount) - sum(p.unit_cost* oi.quantity))/SUM(oi.item_price * oi.quantity - oi.discount_amount) * 100 end gross_margin_pct
from orders o
join order_items oi 
on o.order_id = oi.order_id 
join products p
on oi.product_id = p.product_id
where status = "PAID"
and o.order_datetime between '2025-01-01' and '2025-12-31'
group by p.category 
order by revenue desc
```
**Key Point**
- joined both order_items and products to get the product_id
- Used group by to get the revenue, grss_profit, gross_margin_pct
- Important to handle division by zero for gross_margin_pct