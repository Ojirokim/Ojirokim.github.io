---
title: "Python Practice – Day 44"
date: 2026-04-01
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/string-to-integer-atoi/description/
```python
class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)
        
        while i<n and s[i] == ' ':
            i +=1
        
        sign = 1
        if i < n and s[i] == '-':
            sign = -1
            i +=1
        elif i < n and s[i] == '+':
            sign = 1
            i +=1
        
        num = 0
        while i < n and s[i].isdigit():
            num = num *10 + int(s[i])
            i+= 1

        num *= sign

        smin, smax = -2**31, 2**31 - 1
        return max(smin, min(smax, num))
```

**Key Point**
- control each step of the algorithm starting from blank space.
- check the sign of the number.
- check the number and if it is in the range of 32-bit integer.