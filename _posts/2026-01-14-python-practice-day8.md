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

## Problem 41 — 이상한 문자 만들기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12930
**Difficulty:** Easy

```python
def solution(s):
    result = []
    idx = 0

    for ch in s:
        if ch == " ":
            result.append(ch)
            idx = 0   # reset index at space
        else:
            if idx % 2 == 0:
                result.append(ch.upper())
            else:
                result.append(ch.lower())
            idx += 1

    return "".join(result)
```
**Key Point**
- I misread the question and included the spaces when counting words.
- However, the real question was to count words for each word.


## Problem 42 — 삼총사
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131705
**Difficulty:** Easy

```python
def solution(number):
    answer = 0
    n = len(number)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer
```
**Key Point**
- each line of for allows you to choose each student without selecting them multiple times.


## Problem 43 — 크기가 작은 부분문자열
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/147355
**Difficulty:** Easy

```python
def solution(t, p):
    answer = 0  
    for i in range(len(t)-len(p)+1):
        number = 0
        for x in range(len(p)):
            number += int(t[i+x])*(10**(len(p)-x-1))
        if number <=int(p):
            answer +=1
    return answer
```
**Key Point**
- I did put number =0 outside of for clause which caused an wrong answer.
- I created set of numbers for t then compared them with p


## Problem 44 — 크기가 작은 부분문자열
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/147355
**Difficulty:** Easy

```python
def solution(sizes):
    xlist=[]
    ylist=[]
    for a,b in sizes:
        if a<= b:
            a,b = b,a
        xlist.append(a)
        ylist.append(b)
    answer = max(xlist)*max(ylist)
    return answer
```
**Key Point**
- sorted the list so that each element has [small,big] value.
- Then got the max value from each list.


## Problem 45 — 시저 암호
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12926
**Difficulty:** Easy

```python
def solution(s, n):
    lista=[]
    for i in s:
        x= ord(i)
        if i ==" ":
            lista.append(" ")
            continue
        v=0
        if x<=90:
            if (x+n)>90:
                v=64+(x+n-90)
            else:
                v= x+n
        elif x<= 122:
            if (x+n)>122:
                v=96+(x+n-122)
            else:
                v= x+n
        lista.append(chr(v))
    answer = "".join(lista)
    return answer

```
**Key Point**
- I needed to understand how characters are saved as numbers in python
- ord(char) to turn them into num, chr(number) to change them back into chr
- a corresponding to 97, A corresponding to 65