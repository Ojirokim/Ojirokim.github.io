---
title: "Python Practice – Day 1 (5 Problems)"
date: 2026-01-05
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 1 — 두 수의 차 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120803
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (-50000<=num1 <=50000 and -50000<=num2 <=50000):
        return
    answer = num1-num2 
    return answer
```
**Key Point**
- In order to give condition in a Python language you need to use if statement.
- Used if not, to specify num1, num2 to be inside -50000 and 50000


## Problem 2 — 두 수의 곱 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120804
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (0<=num1 <=100 and 0<=num2<=100):
        return None
    answer = num1*num2
    return answer
```
**Key Point**
- Use if not to give condition to num1, num2
- insight: there were ways to do this with lamda. AMAZING
e.g)
```python
solution = lambda num1, num2 : num1 * num2
```

