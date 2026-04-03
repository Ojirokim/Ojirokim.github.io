---
title: "Programming SQL Practice – Day 36"
date: 2026-04-02
categories: [코드-기술력-자료]
tags: [sql, programmers, daily-practice]
---
---

## 📅 Today’s Goal
- Solve Coding test SQL problems
- Focus on correctness and query structure
---

## Problem 181 - Employees Earning More Than Their Managers
🔗 https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
```sql
select e.name employee
from employee e
left join employee m
on e.managerid = m.id
where e.salary > m.salary
and e.salary is not null
and m.salary is not null
```
**Key Point**
- Self joined the table to get the employee and their manager
- Used where clause to get the employee and their manager


## Problem 182 - Duplicate Emails
🔗 https://leetcode.com/problems/duplicate-emails/description/
```sql
select email
from person
group by email
having  count(*) >=2
```

**Key Point**
- Used having clause to get the duplicate emails