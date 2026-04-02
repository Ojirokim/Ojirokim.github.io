---
title: "Python Practice – Day 45"
date: 2026-04-02
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/palindrome-number/
```python
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        s = str(x)
        n = len(s)
        
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        
        return True
```

**Key Point**
- used `str()` to convert `int` to `str`