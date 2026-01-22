---
title: "Python Practice – Day 14 (3 Problems)"
date: 2026-01-22
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 69 — 성격 유형 검사하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/160586
**Difficulty:** 4

```python
def solution(survey, choices):
    currentpoint={"A":0,"C":0,"F":0,"T":0,"R":0,"J":0,"N":0,"M":0}
    for sur,cho in zip(survey,choices):
        if cho >4:
            currentpoint[sur[1]]+=(cho-4)
        elif cho<4:
            currentpoint[sur[0]]+=(4-cho)
    pairs = [("R","T"), ("C","F"), ("J","M"), ("A","N")]
    answer = ""
    for a, b in pairs:
        answer += a if currentpoint[a] >= currentpoint[b] else b       
    return answer
```
**Key Point**
- Created a dictionary to store each alphabet and its corresponding points
- Input values into the dictionary based on the survey and choices
- Compared the points of each alphabet and returned the answer based on the highest point


## Problem 70 — 바탕화면 정리
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/161990
**Difficulty:** 4

```python

```
**Key Point**
- 