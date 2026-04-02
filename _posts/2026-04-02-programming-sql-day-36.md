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

## Problem 184 — Department Highest Salary
🔗 https://leetcode.com/problems/department-highest-salary/description/
```sql
with sala as(
select d.name department, e.name employee,salary,
rank()over(partition by departmentid order by salary desc) salrank
from Employee e
join department d
on e.departmentid = d.id)
select department, employee, salary
from sala
where salrank = 1
```
**Key Point**
- Used rank() function to get the highest salary of each department
- Used where clause to get the highest salary of each department


## Problem 185 - Department Top Three Salaries
🔗 https://leetcode.com/problems/department-top-three-salaries/
```sql
with high as (
    select d.name department, e.name employee, salary, 
    dense_rank()over(partition by departmentid order by salary desc) salrank
    from employee e
    join department d
    on e.departmentid= d.id
)
select department, employee, salary
from high
where salrank <=3
```

**Key Point**
- Used dense_rank() function to get the top three salaries of each department
- Used where clause to get the top three salaries of each department
- 