---
title: GC Content Analysis
---

## Background

GC content is the fraction of a DNA sequence or set of DNA sequences that is
either a cytosine or a guanine. These two bases, on account of forming three
hydrogen bonds while base pairing in the DNA helix rather than two between
adenine and thymine, influence the biochemical and thermodynamic properties of
the DNA molecule. Different parts of a genome, for example the parts that code
for genes and the intergenic sequences in between, often have different GC
content. In bacteria, the GC content can range from less than 25% to greater
than 75%, depending on the organism. As such, GC content is an important
property of any genome. It is also trivial to compute.

So far we have generated two different sequence subsets from the original
genome: a predicted transcriptome and a synthetic short read dataset. Each of
these sets of sequences has a GC content distribution. The original genome as a
whole also has a total GC content. We will compute and compare the GC contents
of these different sequences.

## Problem statement

Compute the GC content of the original genome and the distribution of GC content
for the predicted transcriptome and synthetic short read dataset.

## Baseline

Write a python script that computes the GC content of a set of sequences. You
might consider writing one script and passing the three different types of
sequences as separate arguments. For the sequences in each file, compute and
record the GC content of each sequence. In the output, report the minimum,
25th percentile, median, 75th percentile, and maximum GC content of the
sequences in each group. The numbers for all of these figures will be identical
for the genome sequence.

### Inputs

* A fasta formatted file of a genome
* The predicted transcriptome fasta file
* The simulated WGS datasets fastq file

### Outputs

* A csv file with the following structure:

  ```
  source,min,pct25,pct50,pct75,max
  genome,.65,.65,.65,.65,.65
  genes,.17,.44,.69,.74,.80
  reads,.05,.25,.65,.71,.88
  ```

### Instructions

### Hints

## Challenge

### Inputs

### Outputs

### Hints
