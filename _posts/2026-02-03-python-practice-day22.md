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

## Problem 86 - H-Index
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42747
**Difficulty:** 4

```python
def solution(citations):
    a = len(citations)
    while 0 <= a:
        templist =[]
        for i in citations:
            if i>=a:
                templist.append(i)
        if len(templist)>=a:
            answer = a
            break
        a -=1
    return answer
```
**Key Point**
- Used `while` loop to find the answer
- Used `list comprehension` to filter the list


## Problem 87 - n^2 배열 자르기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/87390
**Difficulty:** 4
```python
def solution(n, left, right):
    num1 = left//n+1
    num1left = left%n
    num2 = right//n+1
    num2left = n- right%n-1
    anslist = []
    while num1 <= num2:
        anslist.extend([num1]*num1)
        for i in range(n-num1):
            anslist.append(num1+i+1)
        num1 += 1
    if num2left == 0:
        return anslist[num1left:]
    return anslist[num1left:-num2left]
```
**Key Point**
- Created a list of numbers from `left` to `right`
- Used `range()` function to create a list of numbers from `1` to `n`
- Used `extend()` function to add a list to another list