---
title: "Python Practice – Day 11 (5 Problems)"
date: 2026-01-19
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 56 — 과일 장수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/135808
**Difficulty:** Easy

```python
def solution(k, m, score):
    score.sort(reverse=True)
    price =0
    if len(score)<m:
        return 0
    z=len(score)//m
    for x in range(1,(z+1)):
        price1 = score[x*m-1]*m
        price += price1   
    return price

```
**Key Point**
- Used sorting to arrange scores in descending order
- Checked if there are enough scores to form a box
- Calculated total price by multiplying lowest score in each box by box size
- Returned total price as result

