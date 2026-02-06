---
title: "Python Practice – Day 24 (2 Problems)"
date: 2026-02-05
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 2 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem
- Due to the increase in difficulty, I will be solving 2 problems per day.

## Problem 90 - 의상
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42578
**Difficulty:** 4

```python
def solution(clothes):
    clothdic = {}

    for item, category in clothes:
        clothdic.setdefault(category, []).append(item)

    answer = 1
    for items in clothdic.values():
        answer *= (len(items) + 1)

    return answer - 1
```
**Key Point**
- Each category will be given the choice to have 1 or not have.


## Problem 91 - 기능개발
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42586
**Difficulty:** 4
```python
def solution(progresses, speeds):
    answer = []

    while True:
        progresses = [p + s for p, s in zip(progresses, speeds)]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt:
            answer.append(cnt)
        if not progresses:
            break
    return answer
```
**Key Point**
- Used list comprehension to update progresses in one line