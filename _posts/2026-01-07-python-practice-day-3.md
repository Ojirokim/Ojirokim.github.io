---
title: "Python Practice – Day 1 (5 Problems)"
date: 2026-01-06
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 6 — 두 수의 합 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120802
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (-50000<=num1<=50000 and -50000<=num2<=50000):
        return None
    answer = num1+num2
    return answer
```
**Key Point**
- In order to give condition in a Python language you need to use if statement.
- Used if not, to specify num1, num2 to be inside -50000 and 50000

