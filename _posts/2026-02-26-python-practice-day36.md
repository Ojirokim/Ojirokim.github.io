---
title: "Python Practice – Day 36"
date: 2026-02-26
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Instead of codeKata, studying the methods that will be used in the codekata.
- Data Structure & Algorithm

---

### DSA Tutorial
https://www.w3schools.com/dsa/dsa_intro.php

#### Memoization
Technique where results are stored to avoid doing the same computations many times.
When Memoization is used to improve recursive algorithms, 
it is called a "top-down" approach because of how it starts with the main problem and breaks it down into smaller subproblems.

```python
# Fibonacci number with memoization
def F(n):
    if memo[n] != None: # Already computed
        return memo[n]
    else: # Computation needed
        print('Computing F('+str(n)+')')
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = F(n - 1) + F(n - 2)
        return memo[n] 
memo = [None]*7
print('F(6) = ',F(6))
print('memo = ',memo)
```

```python
# AVL Tree with memoization
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
```


#### Tabulation
Tabulation uses a table where the results to the most basic subproblems are stored first. 
The table then gets filled with more and more subproblem results, 
until we find the result to the complete problem that we are looking for.
The tabulation technique is said to solve problems "bottom-up" because of how it solves the most basic subproblems first.
```python
# Fibonacci number with tabulation
def fibonacci_tabulation(n):
    if n == 0: return 0
    elif n == 1: return 1

    F = [0] * (n + 1)
    F[0] = 0 
    F[1] = 1

    for i in range(2, n + 1):
        F[i] = F[i - 1] + F[i - 2]  
    print(F)
    return F[n]
  
n = 10
result = fibonacci_tabulation(n)
print(f"\nThe {n}th Fibonacci number is {result}")
```

#### Dynamic Programming
Divides the problem into subproblems, finds solutions to the subproblems, 
then puts them together to form a complete solution to the problem we want to solve.

##### The problem we want to solve must have these two properties:
Overlapping Subproblems: Means that the problem can be broken down into smaller subproblems, 
where the solutions to the subproblems are overlapping. 
Having subproblems that are overlapping means that the solution to one subproblem is part of the solution to another subproblem.

Optimal Substructure: Means that the complete solution to a problem can be constructed from the solutions of its smaller subproblems. 
So not only must the problem have overlapping subproblems, 
the substructure must also be optimal so that there is a way to piece the solutions to the subproblems together to form the complete solution.

1) bottom-up (tabulation) thinking style
Step 1: Check if the problem has "overlapping subproblems" and an "optimal substructure".
Step 2: Solve the most basic subproblems.
Step 3: Find a way to put the subproblem solutions together to form solutions to new subproblems.

2) top-down (memoization) thinking style
Step 1: Verify DP properties
Step 2: Define the recursive function
--> "What function completely describes the problem?"
Step 3: Write the recurrence
--> "If I knew smaller answers, how would I compute this one?"
Step 4: Define Base Cases
Step 5: Add Memoization Storage
Step 6: Call the main problem


#### Greedy Algorithms
A greedy algorithm decides what to do in each step, only based on the current situation,
without a thought of how the total problem looks like.
Makes the locally optimal choice in each step, hoping to find the global optimum solution in the end.

1) Two properties must be true for a problem for a greedy algorithm to work:
Greedy Choice Property: Means that the problem is so that the solution 
                (the global optimum) can be reached by making greedy choices in each step (locally optimal choices).
Optimal Substructure: Means that the optimal solution to a problem, 
                is a collection of optimal solutions to sub-problems. 
                So solving smaller parts of the problem locally (by making greedy choices) contributes to the overall solution.

