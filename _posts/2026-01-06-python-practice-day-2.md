---
title: "Python Practice – Day 2 (5 Problems)"
date: 2026-01-06
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 6 — 두 수의 합 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120802
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (-50000<=num1<=50000 and -50000<=num2<=50000):
        return None
    answer = num1+num2
    return answer
```
**Key Point**
- In order to give condition in a Python language you need to use if statement.
- Used if not, to specify num1, num2 to be inside -50000 and 50000


## Problem 7 — 두 수의 나눗셈
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120806
**Difficulty:** Easy

```python
def solution(num1, num2):
    if not (0<num1<=100 and 0<num2<=100):
        return None
    answer = int(num1/num2*1000)
    return answer
```
**Key Point**
- floor() rounds down toward negative infinity, 
- while trunc() and int() remove the decimal part by rounding toward zero, 
- which makes them behave differently for negative numbers.


## Problem 8 — 각도기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120829
**Difficulty:** Easy

```python
def solution(angle):
    if 0<angle<90:
        answer = 1
    elif angle== 90:
        answer= 2
    elif  90<angle<180:
        answer = 3
    elif angle==180:
        answer = 4
    return answer
```
**Key Point**
- There is no between function in python only use <,>,=


## Problem 9 — 짝수의 합
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120831
**Difficulty:** Easy

```python
def solution(n):
    if not (0<n<=1000):
        return None
    a= 1
    x=0
    while a < n+1:
        if a%2 == 0:
            x= x+a
        a = a+1
    return x
```
**Key Point**
- You can use While a<x: 
- or you can use for a in range(1,n):
- for clause adds numbers by itself, but while you should add yourself.


## Problem 10 — 배열의 평균값
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/120817
**Difficulty:** Easy

```python
def solution(numbers):
    for a in numbers:
        if not 0<=a<=1000:
            return None
    if not 1<=len(numbers)<=100:
        return None
    answer = sum(numbers)/len(numbers)
    return answer
```
**Key Point**
- Because there is no avg function, you need to use sum() and len()
