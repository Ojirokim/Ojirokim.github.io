---
title: "Python Practice – Day 4 (5 Problems)"
date: 2026-01-08
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 16 — x만큼 간격이 있는 n개의 숫자
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12937
**Difficulty:** Easy

```python
def solution(x, n):
    answert = []
    n = int(n)
    for i in range(1,n+1):
        answert.append(i)
    answer = [int(a)*x for a in answert ]
    return answer
```
**Key Point**
- Used for loop to generate a list and multiply each element by x


## Problem 17 — 자연수 뒤집어 배열로 만들기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12932
**Difficulty:** Easy

```python
def solution(n):
    digits = []
    for x in str(n):
        digits.append(int(x))
    digits.reverse()
    return digits
```
**Key Point**
- for loop to generate a list and reverse it with reverse() method


## Problem 18 — 자연수 뒤집어 배열로 만들기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12932
**Difficulty:** Easy

```python
def solution(n):
    digits = []
    for x in str(n):
        digits.append(int(x))
    digits.reverse()
    return digits
```
**Key Point**
- for loop to generate a list and reverse it with reverse() method

