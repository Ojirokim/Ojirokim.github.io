---
title: "Python Practice – Day 46"
date: 2026-04-03
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/regular-expression-matching/
```python
class Solution(object):
    def isMatch(self, s, p):
        memo = {}

        def match(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                result = (i == len(s))
            else:
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                if j + 1 < len(p) and p[j + 1] == '*':
                    result = match(i, j + 2) or (first_match and match(i + 1, j))
                else:
                    result = first_match and match(i + 1, j + 1)

            memo[(i, j)] = result
            return result

        return match(0, 0)
```

**Key Point**
- Used recursion and memoization to solve the problem

