---
title: "Python Practice – Day 3 (5 Problems)"
date: 2026-01-07
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 11 — 짝수와 홀수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12937
**Difficulty:** Easy

```python
def solution(num):
    if num%2==0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer
```
**Key Point**
- Divide by 2 to check if even or odd


## Problem 12 — 평균 구하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12944
**Difficulty:** Easy

```python
def solution(arr):
    answer = sum(arr) / len(arr)
    return answer
```
**Key Point**
- There is no avg() function in Python so we use sum() and divide by length


## Problem 13 — 자릿수 더하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12931
**Difficulty:** Easy

```python
def solution(n):
    answer = 0
    for x in str(n):
        answer += int(x)
    return answer
```
**Key Point**
- remember to use += when adding numbers to a variable
- turn into string in order to add each digit


## Problem 14 — 약수의 합
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12928
**Difficulty:** Easy

```python
def solution(n):
    t=[]
    x=1
    while x<n+1:
        if n%x ==0:
            t.append(x)
        x +=1
    answer = sum(t)
    return answer
```
**Key Point**
- using while loop to find all the factors of a number.
- then add them with sum()


## Problem 15 — 나머지가 1이 되는 수 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/87389
**Difficulty:** Easy

```python
def solution(n):
    x=1
    while x < n:
        if n%x==1:
            answer = x
            return answer
        x +=1
```
**Key Point**
- using while loop to find the first number that is divisible by 1


