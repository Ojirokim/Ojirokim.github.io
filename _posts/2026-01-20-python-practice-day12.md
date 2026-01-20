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

## Problem 61 — 로또의 최고 순위와 최저 순위
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/77484
**Difficulty:** Easy

```python
from collections import Counter
def solution(lottos, win_nums):
    answer = []
    same_count = sum((Counter(lottos) & Counter(win_nums)).values())
    zero = Counter(lottos)[0]
    high_count = same_count + zero
    if high_count ==0 or high_count==1:
        answer.append(6)
    elif high_count == 2:
        answer.append(5)
    elif high_count == 3:
        answer.append(4)
    elif high_count == 4:
        answer.append(3)
    elif high_count == 5:
        answer.append(2)
    elif high_count == 6:
        answer.append(1)
    if same_count ==0 or same_count==1:
        answer.append(6)
    elif same_count == 2:
        answer.append(5)
    elif same_count == 3:
        answer.append(4)
    elif same_count == 4:
        answer.append(3)
    elif same_count == 5:
        answer.append(2)
    elif same_count == 6:
        answer.append(1)
    return answer
```
**Key Point**
- Utilized Counter to efficiently count occurrences of numbers in both lists
- Can be simplified further by defining another function to count occurrences of numbers in a list
```python
from collections import Counter
def to_rank(cnt):
    if cnt <= 1:
        return 6
    return 7 - cnt
def solution(lottos, win_nums):
    same_count = sum((Counter(lottos) & Counter(win_nums)).values())
    zero = Counter(lottos)[0]
    high_count = same_count + zero
    return [to_rank(high_count), to_rank(same_count)]
```

