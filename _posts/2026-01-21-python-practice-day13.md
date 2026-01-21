---
title: "Python Practice – Day 13 (3 Problems)"
date: 2026-01-21
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 66 — 대충 만든 자판
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/160586
**Difficulty:** 4

```python
def solution(keymap, targets):
    answer=[]
    alpindex={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,
           "Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
    for i in keymap:
        i = i.upper()
        for ind, alp in enumerate(i):
            if alpindex[alp] > (ind+1) or alpindex[alp] == 0:
                alpindex[alp] = (ind+1)
    for x in targets:
            alpcount={"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,
           "Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
            for m in alpcount.keys():
                alpcount[m]=x.count(m)*alpindex[m]
            if any(x.count(ch) > 0 and alpindex[ch] == 0 for ch in alpindex):
                answer.append(-1)
            else:
                answer.append(sum(alpcount.values()))
    return answer
```
**Key Point**
- Created a dictionary to store the index of each alphabet
- Checked if the index of the alphabet is greater than the current index or if it is 0


## Problem 67 — 둘만의 암호
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/160586
**Difficulty:** 4

```python
def solution(s, skip, index):
    answer = []
    skipset = set(ord(ch) for ch in skip)  
    for ch in s:
        num = ord(ch)
        steps = 0
        while steps < index:
            num += 1
            if num > 122:      
                num = 97      
            if num not in skipset:
                steps += 1

        answer.append(chr(num))

    return "".join(answer)
```
**Key Point**
- to put while loop in the for loop
- going back to 97 if the number is greater than 122


## Problem 68 — 대충 만든 자판
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/160586
**Difficulty:** 4

```python
def solution(ingredient):
    ham = [1, 2, 3, 1]
    answer = 0
    y = 0

    while y <= len(ingredient) - 4:
        if ingredient[y:y+4] == ham:
            answer += 1
            del ingredient[y:y+4]
            y = max(0, y - 3)  
        else:
            y += 1

    return answer
```
**Key Point**
- check if the ingredient is equal to ham
- delete the ingredient if it is equal to ham