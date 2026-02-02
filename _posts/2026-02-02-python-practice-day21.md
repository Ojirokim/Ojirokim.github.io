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

## Problem 81 - 괄호 회전하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/76502
**Difficulty:** 4

```python
from collections import deque

def is_valid(dq):
    stack = []
    pair = {')': '(', ']': '[', '}': '{'}

    for ch in dq:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != pair[ch]:
                return False
            stack.pop()

    return not stack

def solution(s):
    n = len(s)
    if n % 2 == 1:
        return 0

    dq = deque(s)
    ans = 0

    for _ in range(n):
        if is_valid(dq):
            ans += 1
        dq.rotate(-1)
    return ans
```
**Key Point**
- Use deque to rotate the string
- Use stack list to check if the string is valid


## Problem 82 - 연속 부분 수열 합의 개수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131701
**Difficulty:** 4

```python
from collections import deque

def solution(elements):
    n = len(elements)
    dq = deque(elements)
    sums = set()

    for length in range(1, n + 1):
        window_sum = sum(list(dq)[:length])
        sums.add(window_sum)

        for _ in range(n - 1):

            out = dq[0]                    
            dq.rotate(-1)                  
            inn = dq[length - 1]            
            window_sum = window_sum - out + inn
            sums.add(window_sum)
    return len(sums)
```
**Key Point**
- Use deque to rotate the string
- Use set to store the sums
- Use sliding window to calculate the sum of each subarray
