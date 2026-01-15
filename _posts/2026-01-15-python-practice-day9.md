---
title: "Python Practice – Day 8 (5 Problems)"
date: 2026-01-15
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 46 — 숫자 문자열과 영단어
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/81301
**Difficulty:** Easy

```python
def solution(s):
    english_dic={'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    for number, english in english_dic.items():
        if english in s:
            s=s.replace(english, number)
    answer = int(s)
    return answer
```
**Key Point**
- Made a dictionary for the comparison.
- Then compared with s and replaced the english into number


## Problem 47 — 문자열 내 마음대로 정렬하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/12915
**Difficulty:** Easy

```python
def solution(strings, n):
    def sort_key(word):
        return (word[n],word)
    return sorted(strings,key=sort_key)
```
**Key Point**
- The important key point here is to understand that sort has more than one argument
- Thus we can use key argument to decide what it sorts with


## Problem 48 — K번째수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42748
**Difficulty:** Easy

```python
def solution(array, commands):
    answer =[]
    for i in commands:
        x= sorted(array[(i[0]-1):(i[1])])[(i[2]-1)]
        answer.append(x)
    return answer
```
**Key Point**
- Finished the job using slicing indexing and sorted() function


## Problem 49 — K번째수
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42748
**Difficulty:** Easy

```python
def solution(numbers):
    answer = []
    for ind, i in enumerate(numbers):
        new_number=numbers[ind+1:]
        for x in (new_number):
                answer.append(i+x)
    answer = sorted(list(set(answer)))
    return answer
```
**Key Point**
- I had to create a new list that have numbers that are not used currently.
- Then got the added value appended to the list.


## Problem 50 — 가장 가까운 같은 글자
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/142086
**Difficulty:** Easy

```python
def solution(s):
    answer=[]
    for ind, i in enumerate(s): 
        if ind ==0:
            answer.append(-1)
        elif i in s[:(ind)]:
            rand=[]
            for inde, t in enumerate(s[:(ind)]):
                if t==i:
                    rand.append(ind-inde)
            answer.append(min(rand))
        else:
            answer.append(-1)
    return answer
```
**Key Point**
- I had to compare each alphabet to the alphabet that comes faster than that one.
- Then picked the one that has the lowest distance.

