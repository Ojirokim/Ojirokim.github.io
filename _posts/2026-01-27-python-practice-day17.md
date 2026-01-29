---
title: "Python Practice – Day 17 (3 Problems)"
date: 2026-01-27
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 78 - 피보나치 수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12939
**Difficulty:** 4

```python
def solution(n):
    answer = 0
    x1 = 0
    x2 = 1
    a = 2
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        while a<=n:
            x3= x1+x2
            x1= x2
            x2= x3
            a +=1
        answer = x3%1234567
    return answer
```
**Key Point**
- Used if statement to check when n is 0 or 1
- else & while statement to calculate the rest of the fibonacci numbers


## Problem 79 - 카펫
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42842
**Difficulty:** 4

```python
import math
def solution(brown, yellow):
    possible =[]
    a = 1
    b = math.sqrt(yellow)
    while a<= b:
        if yellow%a ==0:
                possible.append(a)
        a+=1
    for i in possible:
        x = int(yellow/i)
        if (x+2)*(i+2)-yellow == brown:
            return [x+2,i+2]
    return possible
```
**Key Point**
- Used math.sqrt to calculate the square root of yellow
- Used for loop to check if the number is divisible by each number in possible


## Problem 80 - 예상 대진표
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12985
**Difficulty:** 4

```python
import math
def solution(n, a, b):
    a, b = sorted((a, b))
    num = int(math.log2(n))

    while num > 0:
        block = 2 ** num

        if (a - 1) // block == (b - 1) // block:
            half = 2 ** (num - 1)
            if (a - 1) // half != (b - 1) // half:
                return num
        num -= 1
    return 0
```
**Key Point**
- Used math.sqrt to calculate log2 of n
- Used if statement to check if the number of blocks is equal to the number of blocks in the range