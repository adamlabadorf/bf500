---
title: Algorithms & Complexity
---

1. The Algorithm
    1. An algorithm is a discrete, finite sequence of steps that transforms an
    input into an output
    2. The amount of time it takes an algorithm to complete depends on the number
    of steps it takes
    3. *Algorithmic complexity* is how we reason about the number of steps an
    algorithm takes
2. Algorithmic Complexity
    1. The complexity of an algorithm is measured with respect to the size of
    its inputs
    2. "How many steps must an algorithm complete as a function of its input size?"
    3. e.g. a `for` loop over a list of size $$n$$ has $$n$$ iterations of the loop
    4. A `for` with a `for` inside of it that both loop over a list of size $$n$$
    has $$n \times n$$ or $$n^2$$ steps
    2. Big-O notation, e.g. $$O(n)$$, $$O(n \log n)$$, $$O(n^2)$$
3. Algorithmic Complexity Examples
    1. Search for an item in a unsorted list
    2. Search for an item in a sorted list
    3. Compute all pairs of two lists
    4. Matrix-matrix multiplication
    5. Pearson Correlation
    6. All pairwise correlations of *n* genes with *m* samples?
3. Sidebar: Memory Space Complexity
    1. Similar to algorithmic complexity
    2. "How does the memory required to store a result scale as a function of
    its input size?"
