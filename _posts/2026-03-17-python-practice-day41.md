---
title: "Python Practice – Day 41"
date: 2026-03-17
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/zigzag-conversion/
```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        
        cycle = 2 * numRows - 2
        rows = [''] * numRows
        
        for ind, ch in enumerate(s):
            pos = ind % cycle
            row = pos if pos < numRows else cycle - pos
            rows[row] += ch
        
        return ''.join(rows)
```
**Key Point**
- calculation of cycle was done by multiplying 2 * numRows - 2