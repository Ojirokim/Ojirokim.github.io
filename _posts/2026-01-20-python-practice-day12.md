---
title: "Python Practice – Day 12 (5 Problems)"
date: 2026-01-20
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Solve 5 Python problems
- Focus on correctness + clean structure
- Write 1 key takeaway per problem

---

## Problem 61 — 로또의 최고 순위와 최저 순위
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/77484
**Difficulty:** 3

```python
from collections import Counter
def solution(lottos, win_nums):
    answer = []
    same_count = sum((Counter(lottos) & Counter(win_nums)).values())
    zero = Counter(lottos)[0]
    high_count = same_count + zero
    if high_count ==0 or high_count==1:
        answer.append(6)
    elif high_count == 2:
        answer.append(5)
    elif high_count == 3:
        answer.append(4)
    elif high_count == 4:
        answer.append(3)
    elif high_count == 5:
        answer.append(2)
    elif high_count == 6:
        answer.append(1)
    if same_count ==0 or same_count==1:
        answer.append(6)
    elif same_count == 2:
        answer.append(5)
    elif same_count == 3:
        answer.append(4)
    elif same_count == 4:
        answer.append(3)
    elif same_count == 5:
        answer.append(2)
    elif same_count == 6:
        answer.append(1)
    return answer
```
**Key Point**
- Utilized Counter to efficiently count occurrences of numbers in both lists
- Can be simplified further by defining another function to count occurrences of numbers in a list
```python
from collections import Counter
def to_rank(cnt):
    if cnt <= 1:
        return 6
    return 7 - cnt
def solution(lottos, win_nums):
    same_count = sum((Counter(lottos) & Counter(win_nums)).values())
    zero = Counter(lottos)[0]
    high_count = same_count + zero
    return [to_rank(high_count), to_rank(same_count)]
```


## Problem 62 — 옹알이 (2)
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/133499
**Difficulty:** 3

```python
def solution(babbling):
    answer = 0
    for w in babbling:
        if any(bad in w for bad in ("ayaaya", "yeye", "woowoo", "mama")):
            continue

        for token in ("aya", "ye", "woo", "ma"):
            w = w.replace(token, " ")

        if w.strip() == "":
            answer += 1
    return answer
```

**Key Point**
- using `any()` to check if any substring matches a condition
- using replace() to replace all occurrences of a substring with another string


## Problem 63 — 숫자 짝꿍
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/131128
**Difficulty:** 3

```python
from collections import Counter
def solution(X, Y):
    numbers=[]
    counting = Counter(X)&Counter(Y)
    for k,v in counting.items():
        numbers.extend([k]*v)
    numbers.sort(reverse=True)
    numbers = "".join(numbers)
    if numbers == "":
        answer = "-1"
    elif numbers[0] =="0":
        answer = "0"
    else:
        answer = numbers
    return answer
```

**Key Point**
- Used Counter to efficiently count occurrences of numbers in both lists
- There is a better code that does not use sort and extend
```python
from collections import Counter
def solution(X, Y):
    common = Counter(X) & Counter(Y)

    # Build answer from largest digit to smallest
    result = ''.join(str(d) * common.get(str(d), 0) for d in range(9, -1, -1))

    if not result:
        return "-1"
    if result[0] == "0":
        return "0"
    return result
```


## Problem 64 — 체육복
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/42862
**Difficulty:** 3

```python
def solution(n, lost, reserve):
    new_lost = lost.copy()
    new_reserve = reserve.copy()
    for x in lost:
        if x in new_reserve:
            new_lost.remove(x)
            new_reserve.remove(x)
    new_lost.sort()
    new_reserve.sort()

    for i in new_lost[:]:  
        if i - 1 in new_reserve:
            new_reserve.remove(i - 1)
            new_lost.remove(i)
        elif i + 1 in new_reserve:
            new_reserve.remove(i + 1)
            new_lost.remove(i)
    return n - len(new_lost)
```

**Key Point**
- Sorting the lists before iterating through them is more efficient than iterating through them and sorting each time
- Using `remove()` to remove an element from a list is faster than using `pop()`


## Problem 65 — 문자열 나누기
🔗 https://school.programmers.co.kr/learn/courses/30/lessons/140108
**Difficulty:** 4

```python
def solution(s):
    x=0
    answer = 0
    countsame=0
    countnot=0
    for ind, i in enumerate(s):
        if i == s[x]:
            countsame+=1
        else:
            countnot+=1
        if countsame==countnot:
            x=ind+1
            answer +=1
            countsame=countnot=0
    if countsame!=0:
        answer +=1
    return answer
```

**Key Point**
- Used x to keep track of the index of the last character that was seen
- Used countsame and countnot to count the number of consecutive characters that are the same and not the same