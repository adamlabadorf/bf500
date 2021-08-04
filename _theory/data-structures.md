---
title: Basic Data Structures
---

1. Data structures
    1. For a computer to do things with data, it must be stored in memory (i.e.
    RAM)
    2. Recall from the [Algorithms & Complexity]({{ site.url }}{% link
    _theory/algorithms.md %}) lecture that every algorithm has a complexity
    3. The way data is stored in memory affects the performance of accessing
    elements of that data
    4. Different patterns of storing and accessing data therefore influence how
    efficient our code is
    5. Different patterns of storing and accessing data also influence how easy
    it is for us to write code to use it
2. Basic data structures
    1. lists (or vectors, or arrays)
    2. dictionaries (or associative arrays, or hash maps)
    3. matrices (or arrays)
    4. graphs, and specific types thereof (trees, DAGs, etc)
3. How to know when to use a particular data structure
    1. How do you need to access the elements?
        1. By numeric index? list, or array for more than 1-D
        2. By string key? dictionary
    2. What are the dimensions of the data you need to store?
        1. Scalar? No data structure (i.e. just us a variable)
        2. 1-D? List or array
        3. 2-D? List of lists, matrix
        4. n-D? Arrays
        5. Irregular? Dictionary
    3. What do you need to do to the data?
        1. Numerical operations? Matrix or array
        2. Access random elements quickly? Dictionary, maybe list
        3. Analyze a network? Graph libraries
