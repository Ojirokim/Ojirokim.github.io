---
title: "Python Practice – Day 40"
date: 2026-03-16
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/longest-palindromic-substring/
```python
class Solution(object):
    def longestPalindrome(self, s):
        if not s:
            return ""

        best_start = 0
        best_len = 1

        for i in range(len(s)):

            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > best_len:
                    best_start = left
                    best_len = curr_len
                left -= 1
                right += 1


            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                curr_len = right - left + 1
                if curr_len > best_len:
                    best_start = left
                    best_len = curr_len
                left -= 1
                right += 1

        return s[best_start:best_start + best_len]
```
**Key Point**
- `left` and `right` are the indices of the two palindromic substrings.


