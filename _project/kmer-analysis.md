---
title: k-mer Analysis
---

## Background

A k-mer is a string of length $$k$$, which in genome analysis means a
sequence of DNA bases of that length. In a genome of length $$n$$, there are
$$n-k$$ sequences of length $$k$$, and considering each position in a k-mer
may be one of the four DNA bases, there are $$4^k$$ total possible unique
k-mers. Depending on $$n$$ and $$k$$, you may or may not observe all possible
k-mers in a given genome. The k-mer content of a genome, therefore, is
a measure of the complexity and a fundamental property of that genome. Counting
the number of each k-mer observed in a genome is called k-mer analysis.

## Problem statement

Compute the k-mer content of the genome and list the observed k-mers
from most to least frequently observed.

## Baseline

Perform a 7-mer analysis of the genome using the given genome sequence. Compute
the number of unique k-mers in the genome, the total number of possible unique
7-mers given the value of $$k$$, and the ratio of the two. Then list the 7-mers
by count in descending order.

### Inputs

* A fasta formatted file of a genome

### Outputs

* A `csv` file that contains statistics about the genome length, number of bases,
  and relative base frequencies. Example:

  ```
  key,value
  unique,13519
  total,16384
  perc_observed,0.82513427734375
  ACATAGG,1295
  TCCCATG,1131
  AAGTCCC,1105
  ...
  ```

### Instructions

### Hints

## Challenge

### Inputs

### Outputs

### Hints
