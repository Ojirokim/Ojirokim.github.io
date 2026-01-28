---
title: "Python Practice – Day 16 (3 Problems)"
date: 2026-01-26
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 75 - 최댓값과 최솟값
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12939
**Difficulty:** 4

```python
def solution(s):
    numlist= list(map(int,s.split()))
    return f"{min(numlist)} {max(numlist)}"
```
**Key Point**
- Used map() to convert string to list
- used f-string to return the result

