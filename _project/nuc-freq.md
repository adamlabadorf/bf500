---
title: Nucleotide Frequency Analysis
---

## Background

The nucleotides adenine, cytosine, guanine, and thymine make up the vast majority
of the molecular components of DNA known on the Earth. The relative numbers of
these bases influence the biochemical properties of the DNA molecules they
constitute, including both structure and function. The nucleotide frequency of a
DNA based genome is therefore a fundamental attribute of the molecule and the
organism it specifies.

## Problem statement

Compute the relative nucleotide frequencies of the bases A, C, G, and T in a
given genome.

## Baseline

You will compute the following:

* genome length
* number of each DNA base
* relative nucleotide frequencies for each DNA base

### Inputs

* A fasta formatted file of a genome

### Outputs

* A `csv` file that contains statistics about the genome length, number of bases,
  and relative base frequencies. Example:

  ```
  key,value
  length,1000000
  A,150000
  C,400000
  G,400000
  T,150000
  A_freq,0.15
  C,0.4
  G,0.4
  T,0.15
  ```

### Instructions

### Hints

## Challenge

In addition to the baseline output, you should also compute the dinucleotide
counts and relative frequencies. For all pairs of nucleotides, e.g. `AG`, count
the number of occurrences of these pairs and also compute their relative
frequencies.

### Inputs

* Same as baseline

### Outputs

* In addition to the fields in baseline, also report the dinucleotide counts and
  frequences in your `csv` output file.

### Instructions

### Hints
