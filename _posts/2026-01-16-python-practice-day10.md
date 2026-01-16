---
title: "Python Practice – Day 8 (5 Problems)"
date: 2026-01-15
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 51 — 푸드 파이트 대회
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/134240
**Difficulty:** Easy

```python
def solution(food):
    answer=""
    x=1
    for i in food[1:]:
        if i >=2:
            answer = answer+f"{x}"*(i//2)
        x+=1
    answer_re= answer[::-1]
    answer = answer+"0" + answer_re
    return answer
```
**Key Point**
- Inorder to solve this problem, first made a string for the first eater.
- Then created a string for the second eater by reversing it.
- Then added a 0 to the front of the second eater string.


## Problem 52 — 콜라 문제
🔗 https://www.notion.so/teamsparta/ft-Git-Commit-Push-2e12dc3ef51480029c8ccd0c067a4d12
**Difficulty:** Easy

```python
def solution(a, b, n):
    answer = 0
    while n>=a:
        x= (n//a)*(b)
        n= x + (n%a)
        answer+= x
    return answer
```
**Key Point**
- Created a while loop to solve this problem.


## Problem 53 — 명예의 전당 (1)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/138477
**Difficulty:** Easy

```python
def solution(k, score):
    answer = []
    thelist=[]
    for inde, x in enumerate(score):
        if inde<k:
            thelist.append(x)
        else:
            if min(thelist)<x:
                thelist.append(x)
                thelist.sort()
                thelist=thelist[1:]
        answer.append(min(thelist))
    return answer
```
**Key Point**
- used two lists and a for loop to solve this problem.


## Problem 54 — 2016년
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12901
**Difficulty:** Easy

```python
from datetime import datetime
def solution(a, b):
    time="2016"+f"-{a}-{b}"
    dt = datetime.strptime(time, "%Y-%m-%d")
    new_s = dt.strftime("%a").upper()
    return new_s
```
**Key Point**
- Had a bit of trouble due to not knowing how to use datetime.
- Used strptime and strftime to solve this problem.


## Problem 55 — 카드 뭉치
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/159994
**Difficulty:** Easy

```python
def solution(cards1, cards2, goal):
    i = 0  
    j = 0 

    for word in goal:
        if i < len(cards1) and cards1[i] == word:
            i += 1
        elif j < len(cards2) and cards2[j] == word:
            j += 1
        else:
            return "No"

    return "Yes"
```
**Key Point**
- Got to think about this question one more time.


