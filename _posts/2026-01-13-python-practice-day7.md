---
title: "Python Practice – Day 7 (5 Problems)"
date: 2026-01-13
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 36 — 문자열 다루기 기본
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12918
**Difficulty:** Easy

```python
def solution(s):
    if (len(s) ==4 or len(s)==6) and s.isdigit()==True:
        answer = True
    else:
        answer = False
    return answer
```
**Key Point**
- Found the length of string to compare.
- Found weather the string has only numbers with s.isdigit()


## Problem 37 — 행렬의 덧셈
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12950
**Difficulty:** Easy

```python
def solution(arr1, arr2):
    t=0
    answer = []
    for ar1, ar2 in zip(arr1,arr2):
        answer.append([])
        for a, b in zip(ar1,ar2):
            answer[t].append(a+b)
        t+=1
    return answer
```
**Key Point**
- Had to create a list inside a list using append([])
- then added the elements using appending as well.


## Problem 38 — 직사각형 별찍기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12969
**Difficulty:** Easy

```python
a, b = map(int, input().strip().split(' '))
for x in range(0,b):
    print("*"*a)
```
**Key Point**
- Create a line with * then create a stack of them using for clause.


## Problem 39 — 최대공약수와 최소공배수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12940
**Difficulty:** Easy

```python
def solution(n, m):
    listofnum=[]
    for x in range(1,max(n,m)+1):
        if n%x==0 and m%x==0:
            listofnum.append(x)
    highnum= max(listofnum)
    lownum = n*m/highnum
    answer = [highnum,lownum]
    return answer
```
**Key Point**
- Create a line with * then create a stack of them using for clause.


## Problem 40 — 3진법 뒤집기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/68935
**Difficulty:** Easy

```python
def solution(n):
    x=0
    y=0
    answer = 0
    numlist=[]
    while 3**x <=n:
        x+=1
    for i in range (x-1,-1,-1):
        if n>= 3**i:
            a= n//3**i
            numlist.append(str(a))
            n -= (3**i)*a
        else:
            numlist.append(str(0))
    for number in numlist:
        numnum = int(number)*(3**y)
        y+=1
        answer += numnum
    return answer
```
**Key Point**
- This was a hard one that I had to turn normal number into 3 base number.
- Then I had to turn them back into normal number.

