---
title: "Python Practice – Day 1 (5 Problems)"
date: 2026-01-05
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 1 — 두 수의 차 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120803
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (-50000<=num1 <=50000 and -50000<=num2 <=50000):
        return
    answer = num1-num2 
    return answer
```
**Key Point**
- In order to give condition in a Python language you need to use if statement.
- Used if not, to specify num1, num2 to be inside -50000 and 50000


## Problem 2 — 두 수의 곱 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120804
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (0<=num1 <=100 and 0<=num2<=100):
        return None
    answer = num1*num2
    return answer
```
**Key Point**
- Use if not to give condition to num1, num2
- insight: there were ways to do this with lamda. AMAZING
e.g)
```python
solution = lambda num1, num2 : num1 * num2
```


## Problem 3 — 몫 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120805
**Difficulty:** Easy

```python
import math
def solution(num1, num2):
    if not (0<=num1<=100 and 0<=num2<=100):
        return None
    answer = math.floor(num1/num2)
    return answer
```
**Key Point**
- // also works
- When int() works (no error)
```python
int(3.9)     # 3 truncates values
int("123")   # 123 turning string to int
```
- When int() FAILS (error)
Not string, Not float
```python
int("3.9")   # ValueError
int("abc")   # ValueError
```
- You also need to import math in order to use it.
- This code can also use int() because int() truncates values, which does not need to import math
e.g
```python
def solution(num1, num2):
    if not (0<=num1<=100 and 0<=num2<=100):
        return None
    answer = int(num1/num2)
    return answer
```

## Problem 4 — 나이 출력
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120820
**Difficulty:** Easy

```python
def solution(age):
    if not (0<age<=120):
        return None
    answer = 2023 - age 
    return answer
```
**Key Point**
- I actually tried to make a code that uses the current year using datetime.now()
e.g
```python
from datetime import datetime 
def solution(age):
    if not (0<age<=120):
        return None
    answer = int(datetime.now().strftime('%Y')) - age +1
    return answer
```
I can also improve above code by using .year instead of strftime('%Y')


## Problem 5 — 숫자 비교하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120807
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (0<=num1<=10000 and 0<=num2<=10000):
        return None
    if num1 == num2:
        answer = 1
    else:
        answer = -1
    return answer
```
**Key Point**
- Indentation is not optional in Python.
- I got an error because I indented line 121(answer line) as the same as line 120(if line)