---
title: "Python Practice – Day 14 (3 Problems)"
date: 2026-01-22
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 69 — 성격 유형 검사하기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/160586
**Difficulty:** 4

```python
def solution(survey, choices):
    currentpoint={"A":0,"C":0,"F":0,"T":0,"R":0,"J":0,"N":0,"M":0}
    for sur,cho in zip(survey,choices):
        if cho >4:
            currentpoint[sur[1]]+=(cho-4)
        elif cho<4:
            currentpoint[sur[0]]+=(4-cho)
    pairs = [("R","T"), ("C","F"), ("J","M"), ("A","N")]
    answer = ""
    for a, b in pairs:
        answer += a if currentpoint[a] >= currentpoint[b] else b       
    return answer
```
**Key Point**
- Created a dictionary to store each alphabet and its corresponding points
- Input values into the dictionary based on the survey and choices
- Compared the points of each alphabet and returned the answer based on the highest point


## Problem 70 — 바탕화면 정리
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/161990
**Difficulty:** 4

```python
def solution(wallpaper):
    filesy=[]
    filesx=[]
    for indy, i in enumerate(wallpaper):
        for indx,j in enumerate(i):
            if j == "#":
                filesx.append(indx+1)
                filesy.append(indy+1)
    result = [min(filesy) - 1, min(filesx) - 1, max(filesy), max(filesx)]
    return result
```
**Key Point**
- Created a list to store the x and y coordinates of the files
- Iterated through the wallpaper to find the coordinates of the files
- Calculated the minimum and maximum x and y coordinates
- Returned the result as a list


## Problem 71 — 개인정보 수집 유효기간
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/150370
**Difficulty:** 4

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    today = datetime.strptime(today, "%Y.%m.%d").date()
    answer = []
    dic = {}

    for term in terms:
        term_parts = term.split()
        key = term_parts[0]
        value = int(term_parts[1])  
        dic[key] = value

    for idx, privacy in enumerate(privacies, start=1):
        privacy_parts = privacy.split()
        date_str = privacy_parts[0]
        term_type = privacy_parts[1]
        
        collection_date = datetime.strptime(date_str, "%Y.%m.%d").date()
        expiration_date = collection_date + relativedelta(months=dic[term_type])
        if today >= expiration_date:
            answer.append(idx)
    
    return answer
```
**Key Point**
- Used datetime.strptime to parse the date string into a datetime object
- Used relativedelta to calculate the expiration date
- Used a dictionary to store the terms and their validity periods
- Iterated through the privacies list to check if each privacy is expired
- Appended the index of expired privacies to the answer list
