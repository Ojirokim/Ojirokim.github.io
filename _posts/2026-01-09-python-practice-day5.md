---
title: "Python Practice – Day 5 (5 Problems)"
date: 2026-01-09
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 21 — 하샤드 수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12947
**Difficulty:** Easy

```python
def solution(x):
    a= list(str(x))
    b= [int(i) for i in a]
    B= sum(b)
    if x%B==0:  
        answer = True
    else:
        answer = False
    return answer
```
**Key Point**
- First created a list of the digits in x
- then turned each element into an integer
- finally summed the list


## Problem 22 — 두 정수 사이의 합
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12912
**Difficulty:** Easy

```python
def solution(a, b):
    a, b = sorted([a,b])
    answer = 0
    for x in range(a,b+1):
        answer += x 
    return answer
```
**Key Point**
- First need to sort the two numbers
- Then loop through the range of the numbers and add them up


## Problem 23 — 콜라츠 추측
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12943
**Difficulty:** Easy

```python
def solution(num):
    if num==1:
        return 0
    x=1
    while x<500:
        if num%2==0:
            num= num/2
            if num==1:
                return x
        else:
            num = num*3+1
        x+=1
    return -1
```
**Key Point**
- while loop to find the first number that can be divided by 2 without remainder 
- If the result is 0, return the number of iterations
- If the result is not 0 and when the trial number is 500, return -1


## Problem 24 — 서울에서 김서방 찾기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12919
**Difficulty:** Easy

```python
def solution(seoul):
    a= 0
    for x in seoul:
        if x =="Kim":
            answer = a
        a +=1
    return f"김서방은 {answer}에 있다"
```
**Key Point**
- In order to find the index of the first occurrence of "Kim", we can use a for loop and count the number of times the loop runs
- Then return the answer


## Problem 25 — 나누어 떨어지는 숫자 배열
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12910
**Difficulty:** Easy

```python
def solution(arr, divisor):
    answer = sorted([x for x in arr if x%divisor==0])
    if answer ==[]:
        return [-1]
    else:
        return answer
```
**Key Point**
- found the list of numbers that can be divided evenly by divisor using a list comprehension
- then sorted the list
