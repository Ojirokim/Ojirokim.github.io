---
title: "Python Practice – Day 38"
date: 2026-03-12
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Code Kata related to Data Structure & Algorithm
- solving 1 problems per day
---

## Problem - Algorithm
🔗 https://leetcode.com/problems/two-sum/description/
```python
class Solution(object):
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for j, b in enumerate(nums):
                if i != j and a + b == target:
                    return [i, j]
```

```python
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
```
**Key Point**
- Hash Table used to compare the complement of each number.

## Problem - Algorithm
🔗 https://leetcode.com/problems/add-two-numbers/description/
```python
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```
**Key Point**
- Use dummy node to avoid NoneType error and return the head of the linked list.