---
title: "Python Practice – Day 27"
date: 2026-02-10
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Instead of codeKata, studying the methods that will be used in the codekata.
- Data Structure & Algorithm

---

### DSA Tutorial
https://www.w3schools.com/dsa/dsa_intro.php

### 1. Arrays
#### 1) Bubblesort: algorithm that sorts an array from the lowest value to the highest value.
Compares adjacent elements and swaps them if they are in the wrong order.
The pass through the array is repeated until no swaps are needed, which indicates that the array is sorted.

#### 2) Selctionsort:algorithm finds the lowest value in an array and moves it to the front of the array.
it looks through the array again and again, moving the next lowest values to the front, until the array is sorted.

#### 3) Insertionsort:
It takes each element from the array and places it in its correct position at the correct time.

#### 4) Quicksort:
It divides the array into two smaller sub-arrays.
It then recursively sorts the sub-arrays.
It then combines the sorted sub-arrays to produce the final sorted array.
```python
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)
```

```python
fib_array = [0, 1]  # 피보나치 수열의 시작 두 값을 배열에 저장, 초기 값은 0, 1 

def memo_fibonacci_arr(n):  # 메모이제이션을 이용한 피보나치 함수 선언 n은 계산하고자 하는 피보나치 수의 인덱스
    if n < len(fib_array):  # 만약 요청된 n이 이미 계산된 범위 내에 있다면,
        return fib_array[n]  # 메모이제이션된 결과를 반환
        
    else:  # 만약 n이 계산된 범위 밖에 있다면,
        fib = memo_fibonacci_arr(n-1) + memo_fibonacci_arr(n-2)  # 재귀적으로 (n-1)과 (n-2)번째 피보나치 수를 계산
        fib_array.append(fib)  # 계산된 피보나치 수를 배열에 추가 이는 추후 동일한 값이 요청될 때 중복 계산을 방지하기위해
        return fib  # 계산된 피보나치 수를 반환
```

```python
def memo_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    # if n == 1 or n == 2:
    #     return 1
    
    memo[n] = memo_fibonacci(n - 1, memo) + memo_fibonacci(n - 2, memo)
    return memo[n]
```

#### 5) Countingsort:
It counts the number of occurrences of each unique value in an array.
It then constructs an array containing each unique value as an index.

#### 6) Radixsort:
It sorts numbers by grouping digits by their individual digits and then sorting within each group using a counting sort.
Must use a stable sorting algorithm.
```python
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(myArray)
exp = 1

while maxVal // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array:", myArray)
```