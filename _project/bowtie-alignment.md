---
title: bowtie Alignment
---

## Background

The short sequences in a high throughput sequencing dataset represent the
nucleotide sequences of short DNA fragments in the original sample. When the
source genome sequence is available, it should in principle be possible to
locate the region of the genome where each DNA fragment originated. The process
of finding how one sequence matches against another sequence is called
*alignment* or *mapping* and is a fundamental operation in bioinformatics.
Specialized algorithms for aligning short sequences, like reads, against a much
longer reference genome have been available for many years and the software
packages that implement them are open source and very mature.
[bowtie](http://bowtie-bio.sourceforge.net/index.shtml) is one such alignment
program that we will use to align our synthetic WGS reads back to our original
genome.

bowtie aligns short reads against a reference genome very efficiently. This is
due to a specific algorithm and corresponding data structure, called the
[Burrows Wheeler Transform](https://en.wikipedia.org/wiki/Burrows%E2%80%93Wheeler_transform),
that makes searching for short sequences of text in a much larger database of
text very fast. Therefore, before using bowtie to align short reads against a
genome, the genome must first be transformed from its native sequence fasta
format to this specialized format by bowtie. The process of preparing a genome
sequence for this purpose is called creating an *index* of the genome. This
index need only be created once for each genome and may then be used repeatedly
when aligning samples against it.

## Problem statement

Align the simulated reads against the reference genome.

## Baseline

Align the simulated reads against the reference genome using bowtie. You will
need to *index* the genome first using the appropriate tool in the bowtie
package. Store the result in SAM format.

### Inputs

* A fasta formatted file of a genome
* The simulated WGS datasets

### Outputs

* A SAM formatted file containing alignments of the WGS reads against the genome

### Instructions

### Hints

## Challenge

Once you have aligned the reads against the genome, use the gff annotation you
made with RAST to count the number of reads mapping to each annotated gene.

### Inputs

### Outputs

### Hints
