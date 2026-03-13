---
title: "Python Practice – Day 38"
date: 2026-02-26
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 2 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/two-sum/description/
```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        word_dict = {}
        max_length = 0

        for ind, alpha in enumerate(s):
            if alpha in word_dict and word_dict[alpha] >= left:
                left = word_dict[alpha] + 1

            word_dict[alpha] = ind
            max_length = max(max_length, ind - left + 1)

        return max_length
```
**Key Point**
- `word_dict` is a dictionary that stores the index of each character in the string.
- `left` is the index that checks the last character with the dictionary.


## Problem - Algorithm
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            i = (left + right) // 2
            j = half - i

            nums1_left  = nums1[i-1] if i > 0 else float('-inf')
            nums1_right = nums1[i]   if i < m else float('inf')

            nums2_left  = nums2[j-1] if j > 0 else float('-inf')
            nums2_right = nums2[j]   if j < n else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)

                return (max(nums1_left, nums2_left) +
                        min(nums1_right, nums2_right)) / 2.0

            elif nums1_left > nums2_right:
                right = i - 1

            else:
                left = i + 1
```
**Key Point**
- `left` and `right` are the indices of the two sorted arrays.
