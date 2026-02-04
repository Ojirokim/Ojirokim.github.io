---
title: "Python Practice – Day 21 (2 Problems)"
date: 2026-02-02
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 2 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem
- Due to the increase in difficulty, I will be solving 2 problems per day.

## Problem 88 - 
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42747
**Difficulty:** 4

```python
def solution(arr1, arr2):
    rows1 = len(arr1)
    cols1 = len(arr1[0])
    cols2 = len(arr2[0])

    answer = []
    for r in range(rows1):
        row = []
        for c in range(cols2):
            s = 0
            for k in range(cols1):
                s += arr1[r][k] * arr2[k][c]
            row.append(s)
        answer.append(row)
    return answer
```
**Key Point**
- Used 3 for loops to solve the problem


## Problem 89 - 
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/87390
**Difficulty:** 4
```python
from collections import Counter
def solution(want, number, discount):
    answer = 0
    d = dict(sorted(dict(zip(want, number)).items()))
    for i in range(len(discount) - 9):
        tempdic= dict(sorted(Counter(discount[i:i+10]).items()))
        if tempdic.keys() >= d.keys() and all(d[k] <= tempdic[k] for k in d):
            answer +=1
    return answer
```
**Key Point**
- used Counter to count the number of each item in a list