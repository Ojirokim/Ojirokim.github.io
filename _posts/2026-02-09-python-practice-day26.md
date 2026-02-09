---
title: "Python Practice – Day 26 (2 Problems)"
date: 2026-02-09
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 2 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 92 - 프로세스
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42587
**Difficulty:** 4
```python
def solution(priorities, location):
    order = []
    while max(priorities) !=0:
        for ind, val in enumerate(priorities):
            if val == max(priorities) and ind not in order:
                order.append(ind)
                priorities[ind] = 0
    return order.index(location)+1
```
**Key Point**
- Used for loop inside while loop to find the index of the location
- Used max() to find the maximum value in the list


## Problem 93 - 피로도
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/87946
**Difficulty:** 5
```python
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    ans = 0

    def dfs(fatigue, cnt):
        nonlocal ans
        ans = max(ans, cnt)

        for i in range(n):
            req, cost = dungeons[i]
            if not visited[i] and fatigue >= req:
                visited[i] = True
                dfs(fatigue - cost, cnt + 1)
                visited[i] = False

    dfs(k, 0)
    return ans
```
**Key Point**
- Tried every combination of the dungeons and found the maximum value of the count