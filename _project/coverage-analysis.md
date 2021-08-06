---
title: Coverage Analysis
---

## Background

When aligning a short read dataset against a genome, there are two important
statistics we compute to assess the quality of the dataset. The first is
*coverage*. Recall that a WGS dataset contains fragments of DNA that originated
from a contiguous genome. The DNA fragments that were sequenced were sampled
randomly, so that sometimes some parts of the genome were captured more often
than others. If an insufficient number of reads were generated for the length
of the originating genome, some portions of the genome might not be represented
by any reads at all. Such portions of the genome are not "covered" by the
dataset. Therefore the *coverage* of a dataset is the fraction of the
original genome that has at least one read mapping to it. A dataset with 100%
coverage has at least one read mapping to every base of the genome; in a dataset
with only 60% coverage, only 60% of the bases of the original genome were
captured by reads.

The second related statistic of a dataset is *depth*. When considering a single
base position of the original genome, the *read depth* of that location is
simply the number of reads that contain that base position. For example, if
one position in the genome has 20 reads that map to it, that position has a
depth of 20; another position with just 2 reads mapping to it has a depth of
only 2. Since the DNA molecules sequenced are sampled randomly from the genome,
the depth of positions across the whole genome varies. The depth of an entire
dataset is usually defined as the *average depth* across all positions in the
genome.

Since we have aligned our synthetic reads against the genome, we can use the
resulting alignments to compute both the *coverage* and *depth* of the dataset.
Fortunately, another open source and mature tool called
[samtools](http://www.htslib.org/) provides these functions for us.

## Problem statement

Compute the coverage and depth statistics for the aligned synthetic reads
against the genome.

## Baseline

Use the `samtools depth` tool to compute the read depth for the entire genome
using your bowtie alignments. Note that this tool requires the reads to be
sorted by base position first, so sort your SAM file with the `samtools sort`
command prior to computing depth.

The samtools depth tool produces a file with information about the number of
reads that map to each position in the genome. We wish to compute summary
statistics, including % coverage and average depth and so much post process
this file. Write a python script to read in the contents of the depth file,
compute these statistics, and write them out to a csv file. Your csv should
have the following values:

* `coverage`: the calculated coverage of reads over the genome, expressed as a
  number between 0 and 1
* `average_depth`: the average read depth across the entire genome, expressed as
  an integer
* The remaining rows of the file have a depth in the first column and the number
  of bases in the genome with that depth in the second column. For example, the
  there maybe only 312 positions in the genome that have only one read mapping
  to them, but 35,250 positions with 20 reads mapping to them. The depth values
  reported in your file should be in ascending order, i.e. report the positions
with a depth of 1, then depth of 2, and so on.

### Inputs

* SAM formatted alignments of the synthetic reads from bowtie

### Outputs

* `samtools depth` output
* A csv file with the following structure:

  ```
  key,value
  coverage,0.998315
  average_depth,22
  1,312
  2,553
  3,790
  ...
  ```

### Instructions

### Hints

## Challenge

### Inputs

### Outputs

### Hints
