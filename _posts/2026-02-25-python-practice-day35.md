---
title: "Python Practice – Day 35"
date: 2026-02-25
categories: [코드-기술력-자료]
tags: [python, daily-practice]
---

## 📅 Today’s Goal
- Instead of codeKata, studying the methods that will be used in the codekata.
- Data Structure & Algorithm

---

### DSA Tutorial
https://www.w3schools.com/dsa/dsa_intro.php

#### Eculidean Algorithm
When you divide the first number by the second, 
the remainder is just the first number minus some multiple of the second. 
Any number that divides both original numbers will also divide that remainder. 
And any number that divides the second number and the remainder will also divide the first number.
So the set of common divisors stays exactly the same.

The algorithm simply repeats this idea. Each step replaces the bigger pair of numbers with a smaller pair: 
the previous divisor and the remainder. 
The greatest common divisor never changes during this process — only the numbers get smaller.
Eventually, you reach a step where the remainder becomes zero. At that moment, 
the last non-zero remainder divides the number before it exactly. 
That means it is the greatest number that divides both. 
Since the greatest common divisor never changed throughout the process, 
that last non-zero remainder must be the greatest common divisor of the original two numbers.

```python
def gcd_division(a, b):
    while b != 0:
        remainder = a % b
        print(f"{a} = {a//b} * {b} + {remainder}")
        a = b
        b = remainder
    return a

a = 120
b = 25
print("The Euclidean algorithm using division:\n")
print(f"The GCD of {a} and {b} is: {gcd_division(a, b)}")
```

#### Huffman Coding
Huffman coding is a greedy algorithm used to create an optimal prefix-free binary code based on symbol frequencies
Symbols that appear more frequently should have shorter binary codes.
Symbols that appear less frequently should have longer codes.

Huffman Code Prefixes:
No code is the prefix of another code, makes it possible to decode. 
And it is especially important in Huffman Coding because of the variable bit lengths.

```python
# Huffman Coding
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

def calculate_frequencies(word):
    frequencies = {}
    for char in word:
        if char not in frequencies:
            freq = word.count(char)
            frequencies[char] = freq
            nodes.append(Node(char, freq))

def build_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        nodes.append(merged)

    return nodes[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_huffman_codes(node.left, current_code + '0', codes)
    generate_huffman_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = build_huffman_tree()
    codes = {}
    generate_huffman_codes(root, '', codes)
    return codes

word = "lossless"
codes = huffman_encoding(word)
encoded_word = ''.join(codes[char] for char in word)

print("Word:", word)
print("Huffman code:", encoded_word)
print("Conversion table:", codes)
```

```python
# Huffman Decoding
class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

nodes = []

def calculate_frequencies(word):
    frequencies = {}
    for char in word:
        if char not in frequencies:
            freq = word.count(char)
            frequencies[char] = freq
            nodes.append(Node(char, freq))

def build_huffman_tree():
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        nodes.append(merged)

    return nodes[0]

def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code

    generate_huffman_codes(node.left, current_code + '0', codes)
    generate_huffman_codes(node.right, current_code + '1', codes)

def huffman_encoding(word):
    global nodes
    nodes = []
    calculate_frequencies(word)
    root = build_huffman_tree()
    codes = {}
    generate_huffman_codes(root, '', codes)
    return codes

def huffman_decoding(encoded_word, codes):
    current_code = ''
    decoded_chars = []

    # Invert the codes dictionary to get the reverse mapping
    code_to_char = {v: k for k, v in codes.items()}

    for bit in encoded_word:
        current_code += bit
        if current_code in code_to_char:
            decoded_chars.append(code_to_char[current_code])
            current_code = ''

    return ''.join(decoded_chars)

word = "lossless"
codes = huffman_encoding(word)
encoded_word = ''.join(codes[char] for char in word)
decoded_word = huffman_decoding(encoded_word, codes)

print("Initial word:", word)
print("Huffman code:", encoded_word)
print("Conversion table:", codes)
print("Decoded word:", decoded_word)
```

Compression creates a trade-off between computation and data size.
When we compress data:
CPU usage increases (more computation is needed to encode and decode).
Bandwidth usage decreases (less data needs to be transmitted).
Storage usage decreases (less space is required to store the data).
So in practice, we trade computational effort for reduced data size.
This is not a strict mathematical negative relationship, but a systems-level trade-off. 
Whether compression is beneficial depends on the context — such as network speed, storage cost, and how compressible the data is.
In most real-world systems, the cost of extra computation is smaller than the benefit of reduced transmission and storage, so compression is worth it.


#### Traveling Salesman Problem
Except for the Held-Karp algorithm (which is quite advanced and time consuming, and will not be described here)
There is no other way to find the shortest route than to check all possible routes.
This means that the time complexity for solving this problem is O(n!).

There are other Algorithms that can solve this problem in O(n^2) time.
However, they are not as efficient as the Held-Karp algorithm and they do not guarantee the shortest route.


#### The 0/1 Knapsack Problem
Problem states that you have a backpack with a weight limit, 
and you are in a room full of treasures, each treasure with a value and a weight.
1) The Brute Force Approach
usually the most straight forward way of solving a problem, but it also requires the most calculations.

2) Memoization(Top-Down Approach)
The idea is to store the previous function call results in an array, 
so that previous results can be fetched from that array and does not have to be calculated again.
```python
def knapsack_memoization(capacity, n):
    print(f"knapsack_memoization({n}, {capacity})")
    if memo[n][capacity] is not None:
        print(f"Using memo for ({n}, {capacity})")
        return memo[n][capacity]
    
    if n == 0 or capacity == 0:
        result = 0
    elif weights[n-1] > capacity:
        result = knapsack_memoization(capacity, n-1)
    else:
        include_item = values[n-1] + knapsack_memoization(capacity-weights[n-1], n-1)
        exclude_item = knapsack_memoization(capacity, n-1)
        result = max(include_item, exclude_item)

    memo[n][capacity] = result
    return result

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
n = len(values)
memo = [[None]*(capacity + 1) for _ in range(n + 1)]
print("\nMaximum value in Knapsack =", knapsack_memoization(capacity, n))
```

3) The Tabulation Approach (bottom-up)
Solving the 0/1 Knapsack problem is to use something called tabulation. 
This approach is also called the iterative approach, and is a technique used in Dynamic Programming.
```python
def knapsack_tabulation():
    n = len(values)
    tab = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                include_item = values[i-1] + tab[i-1][w - weights[i-1]]
                exclude_item = tab[i-1][w]
                tab[i][w] = max(include_item, exclude_item)
            else:
                tab[i][w] = tab[i-1][w]

    for row in tab:
        print(row)

    items_included = []
    w = capacity
    for i in range(n, 0, -1):
        if tab[i][w] != tab[i-1][w]:
            items_included.append(i-1)
            w -= weights[i-1]

    print("\nItems included:", items_included)

    return tab[n][capacity]

values = [300, 200, 400, 500]
weights = [2, 1, 5, 3]
capacity = 10
print("\nMaximum value in Knapsack =", knapsack_tabulation())
```
