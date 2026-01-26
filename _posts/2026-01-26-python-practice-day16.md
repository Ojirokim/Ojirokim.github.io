---
title: "Python Practice – Day 16 (3 Problems)"
date: 2026-01-26
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 75 - 최댓값과 최솟값
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12939
**Difficulty:** 4

```python
def solution(s):
    numlist= list(map(int,s.split()))
    return f"{min(numlist)} {max(numlist)}"
```
**Key Point**
- Used map() to convert string to list
- used f-string to return the result


## Problem 76 - JadenCase 문자열 만들기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12951
**Difficulty:** 4

```python
def solution(s):
    wordlist = s.split(" ")
    for idx, word in enumerate(wordlist):
        word = word.lower()
        if word and word[0].isalpha():
            word = word[0].upper() + word[1:]
        wordlist[idx] = word
    return " ".join(wordlist)
```
**Key Point**
- Used isalpha() to check if the first character is an alphabet
- Used string slicing to capitalize the first character and concatenate with the rest of the word


## Problem 77 - 이진 변환 반복하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/70129
**Difficulty:** 4

```python
def solution(s):
    zero = 0
    times=0
    while int(s)>1:
        zero += s.count("0")
        s= s.count("1")
        s=bin(s)[2:]
        times+=1
    return [times, zero]
```
**Key Point**
- Used bin()[2:] to convert binary number to decimal
- Used count() to count the number of "0"s and "1"s
