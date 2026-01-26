---
title: "Python Practice – Day 15 (3 Problems)"
date: 2026-01-23
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 3 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 72 - 달리기 경주
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/178871
**Difficulty:** 4

```python
def solution(players, callings):
    pos = {player: i for i, player in enumerate(players)}

    for name in callings:
        i = pos[name]
        j = i - 1
        front = players[j]

        players[j], players[i] = players[i], players[j]

        pos[name] = j
        pos[front] = i

    return players
```
**Key Point**
- My original solution which I wrote below was not wrong, but it was not efficient.
- I learned that changing the way how I stored the position of players in a dictionary is more efficient than doing a full loop.
```python
def solution(players, callings):
    for person in callings:
        x= players.index(person)
        players[x], players[x-1] = players[x-1], players[x]
    return players
```


## Problem 73 - 공원산책
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/172928
**Difficulty:** 4

```python
def solution(park, routes):
    blocks = []
    H, W = len(park), len(park[0])

    for r, row in enumerate(park):
        for c, cell in enumerate(row):
            if cell == "S":
                pos = [r, c]
            elif cell == "X":
                blocks.append([r, c])
    for route in routes:
        direct, num = route.split()
        num = int(num)
        dr, dc = 0, 0
        if direct == "E": dc = 1
        elif direct == "W": dc = -1
        elif direct == "S": dr = 1
        elif direct == "N": dr = -1
        nr, nc = pos[0], pos[1]
        ok = True

        for _ in range(num):
            nr += dr
            nc += dc
            if not (0 <= nr < H and 0 <= nc < W):
                ok = False
                break
            if [nr, nc] in blocks:
                ok = False
                break
        if ok:
            pos = [nr, nc]
    return pos
```
**Key Point**
- Using for loop to iterate through the park to create a list of blocks and current position.
- Then used another for loop to iterate through the routes to move the position.


## Problem 74 - 신고 결과 받기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/92334
**Difficulty:** 4
```python
from collections import Counter

def solution(id_list, report, k):
    report = set(report)    
    reports_by_user = {user: [] for user in id_list}
    reported_count = {user: 0 for user in id_list}
    
    for r in report:
        reporter, target = r.split()
        reports_by_user[reporter].append(target)
        reported_count[target] += 1

    banned_users = {user for user, count in reported_count.items() if count >= k}
    
    answer = []
    for user in id_list:
        mail_count = 0
        for target in reports_by_user[user]:
            if target in banned_users:
                mail_count += 1
        answer.append(mail_count)
        
    return answer
```

**Key Point**
- Using Counter to count the number of reports for each user.
- Then using set to remove the users who have reported more than k times.