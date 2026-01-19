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

## Problem 56 — 과일 장수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/135808
**Difficulty:** Easy

```python
def solution(k, m, score):
    score.sort(reverse=True)
    price =0
    if len(score)<m:
        return 0
    z=len(score)//m
    for x in range(1,(z+1)):
        price1 = score[x*m-1]*m
        price += price1   
    return price

```
**Key Point**
- Used sorting to arrange scores in descending order
- Checked if there are enough scores to form a box
- Calculated total price by multiplying lowest score in each box by box size
- Returned total price as result


## Problem 57 — 모의고사
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42840
**Difficulty:** Easy

```python
def solution(answers):
    real_answer=[]
    correct_stu=[]
    check=0
    num1=[1,2,3,4,5]
    num2=[2,1,2,3,2,4,2,5]
    num3=[3,3,1,1,2,2,4,4,5,5]
    for ind, answer in enumerate(answers):
        if answer == num1[(ind%(len(num1)))]:
            check +=1
    correct_stu.append(check)
    check = 0
    for ind, answer in enumerate(answers):
        if answer == num2[(ind%(len(num2)))]:
            check +=1
    correct_stu.append(check)
    check = 0
    for ind, answer in enumerate(answers):
        if answer == num3[(ind%(len(num3)))]:
            check +=1
    correct_stu.append(check)
    for i, x in enumerate(correct_stu):
        if x== max(correct_stu):
            real_answer.append(i+1)
    return real_answer
```
**Key Point**
- Created 3 lists to store answers for each question
- Used modulo operator to determine which list each answer belongs to
- Appended the index of the correct list to a new list
- Returned the index of the correct list as result


## Problem 58 — 소수 만들기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12977
**Difficulty:** Easy

```python
from itertools import combinations
def solution(nums):
    answer = 0
    numbers =[sum(c) for c in combinations(nums, 3)]
    for x in numbers:
        reasoning = True
        for i in range(x):
            if i<2:
                continue
            else:
                if x%i == 0:
                    reasoning = False
                    break
        if reasoning:
            answer +=1
    return answer
```
**Key Point**
- used itertools.combinations to generate all possible combinations of 3 numbers
- Checked if each combination is prime by dividing each number by all other numbers


## Problem 59 — 덧칠하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/161989
**Difficulty:** Easy

```python
def solution(n, m, section):
    count = 0
    covered_until = 0

    for s in section:
        if s > covered_until:
            count += 1
            covered_until = s + m - 1
    return count
```
**Key Point**
- Counted the number of sections that need to be covered
- Used a variable to keep track of the last section that was covered


## Problem 60 — 기사단원의 무기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/136798
**Difficulty:** Easy

```python
def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        amount = 0
        for j in range(1, i+1):
            if i%j==0:
                amount += 1
        if amount > limit:
            answer += power
        else:
            answer += amount
return answer
```
**Key Point**
- Created a loop to count the number of divisors for each number
- Used an if statement to check if the number of divisors exceeded the limit
- There is a better way to do this by checking the number of divisors in advance and storing them in a list
```python
def solution(number, limit, power):
    divs = [0] * (number + 1)

    for d in range(1, number + 1):
        for multiple in range(d, number + 1, d):
            divs[multiple] += 1

    answer = 0
    for i in range(1, number + 1):
        answer += power if divs[i] > limit else divs[i]
    return answer
```

