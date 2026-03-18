---
title: "Python Practice – Day 42"
date: 2026-03-18
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/reverse-integer/
```python
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        reversed_num = int(str(x_abs)[::-1])

        if len(str(reversed_num)) < 10:
            return sign * reversed_num

        if sign == 1:
            limit = "2147483647"
        else:
            limit = "2147483648"

        reversed_str = str(reversed_num)

        for i in range(10):
            if reversed_str[i] < limit[i]:
                return sign * reversed_num
            elif reversed_str[i] > limit[i]:
                return 0

        return sign * reversed_num
```
**Key Point**
- Created a reverse number than check if it is within the limit.