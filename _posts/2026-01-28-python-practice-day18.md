---
title: "Python Practice – Day 18 (3 Problems)"
date: 2026-01-28
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 81 - 최댓값과 최솟값
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12939
**Difficulty:** 4

```python
import math

def solution(arr):
    lcm = arr[0]
    for n in arr[1:]:
        lcm = lcm * n // math.gcd(lcm, n)
    return lcm
```
**Key Point**
- Using gcd() is the main point of solving this problem


## Problem 82 - 멀리 뛰기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12914
**Difficulty:** 4

```python
def solution(n):
    a1 = 1
    a2 = 2
    x=3
    if n ==1:
        answer = 1
    elif n == 2:
        answer = 2
    while x<=n:
        answer = a1+a2
        a1 = a2
        a2 = answer
        x +=1
    return answer%1234567
```
**Key Point**
- Use dynamic programming to calculate the nth Fibonacci number efficiently


## Problem 83 - 귤 고르기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/138476
**Difficulty:** 4

```python
from collections import Counter
def solution(k, tangerine):
    c=Counter(tangerine)
    clist = c.most_common()
    a=0
    for i in range(len(clist)):
        a += clist[i][1]
        if a >= k:
            answer = i+1
            break
    return answer
```
**Key Point**
- Used Counter() to count the frequency of each fruit



