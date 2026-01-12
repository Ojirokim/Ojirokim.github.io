---
title: "Python Practice – Day 6 (10 Problems)"
date: 2026-01-12
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 10 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 26 — 음양 더하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/76501
**Difficulty:** Easy

```python
def solution(absolutes, signs):
    alist=[]
    for num, sign in zip(absolutes, signs):
        if sign == True:
            alist.append(num)
        else:
            alist.append(num*-1)
    answer = sum(alist)
    return answer
```
**Key Point**
- Create an for line to take one element from each list.
- Then append num from absolutes and multiply -1 or 1 based on the value in signs.


## Problem 27 — 핸드폰 번호 가리기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12948
**Difficulty:** Easy

```python
def solution(phone_number):
    length= len(phone_number[0:-4])
    answer = "*"*length+phone_number[-4:]
    return answer
```
**Key Point**
- First find out how long the numbers are with len().
- Then replace it with *


## Problem 28 — 없는 숫자 더하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/86051
**Difficulty:** Easy

```python
def solution(numbers):
    answer_list=[]
    for x in range(0,10):
        if x not in numbers:
            answer_list.append(x)
    answer = sum(answer_list)
    return answer
```
**Key Point**
- Find the numbers inside that is not in numbers using for and if clause.


## Problem 29 — 제일 작은 수 제거하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12935
**Difficulty:** Easy

```python
def solution(arr):
    if arr == [10]:
        answer = [-1]
    else:
        arr_min = min(arr)
        arr.remove(arr_min)
        answer = arr
    return answer
```
**Key Point**
- If the given arr is [10] then provide the answer [-1]
- If not provide the answer with the lowest value deleted.


## Problem 30 — 가운데 글자 가져오기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12903
**Difficulty:** Easy

```python
def solution(s):
    if len(s)%2==0:
        a= len(s)//2 -1
        b= a +2
        answer = s[a:b]
    else:
        a= len(s)//2
        answer = s[a]
    return answer
```
**Key Point**
- I should remember that slicing looks like [::] not [,] which made an error.
- Also need to use // instead of / due to / creating a float instead of an int.


## Problem 31 — 수박수박수박수박수박수?
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12922
**Difficulty:** 2

```python
def solution(n):
    if n%2==0:
        answer = "수박"*(n//2)
    else:
        answer = "수" + "박수"*(n//2)
    return answer
```
**Key Point**
- Divided the case into odd number and even number.
- Then provided the answer for each one.


## Problem 32 — 내적
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/70128
**Difficulty:** 2

```python
def solution(a, b):
    ablist=[]
    for x, y in zip(a,b):
        ablist.append(x*y)
    answer= sum(ablist)
    return answer
```
**Key Point**
- Used zip() to get each element from each list.
- Then added them to an empty list.
- Then summed it up


## Problem 33 — 약수의 개수와 덧셈
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/77884
**Difficulty:** 2

```python
def solution(left, right):
    numlist = []
    for x in range(left, right+1):
        tempxlist =[]
        for i in range (1,x+1):
            if x%i == 0:
                tempxlist.append(i)
        if len(tempxlist)%2==0:
            numlist.append(x)
        else:
            numlist.append(-x)
    answer = sum(numlist)
    return answer
```
**Key Point**
- Had to use two for clause in order to use each number between left and right and to get the divisor. 


## Problem 34 — 문자열 내림차순으로 배치하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12917
**Difficulty:** 2

```python
def solution(s):
    s=sorted(s)
    answer = s[::-1]
    answer = "".join(answer)
    return answer
```
**Key Point**
- use sorted() to sort the string. 
- Then combine them again using join


## Problem 35 — 족한 금액 계산하기

🔗 https://school.programmers.co.kr/learn/courses/30/lessons/82612
**Difficulty:** 2

```python
def solution(price, money, count):
    x=0
    for i in range(0,count+1):
        x += i
    full_price = x* price
    if full_price >money:
        answer = full_price - money
    else:
        answer = 0
    return answer
```
**Key Point**
- If the calculate the full price first using for clause.
- Then compare it with money to get the answer.





