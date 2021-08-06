---
title: WGS Read Simulation
---

## Background

With its advent in the mid 2000s, high throughput sequencing technology
dramatically accelerated our ability to rapidly determine the nucleotide
sequences of DNA and RNA at very low cost. This requires expensive and
sophisticated instruments that can only determine the nucleotide sequence of
relatively short DNA molecules, where the most popular and cost effective
technology at the time of writing (Illumina) can sequence molecules of most 300
nucleotides in length. Although the sequences are short, many millions of these
short molecules can be sequenced at once, producing huge amounts of data that
can be combined with bioinformatic algorithms to glean biological insight from
the sequences. One such flavor of high throughput sequencing data is *Whole
Genome Sequencing* (WGS) where the complete repertoire of DNA in an organism is
subjected to high throughput sequencing technology. The resulting short reads
can be analyzed in such a way as to reconstruct very large portions of, and
possibly the entire genome sequence.

Although WGS sequencing datasets for our organism may already exist, we will
instead simulate some data by sampling short sequences from the larger genome.
Simulating reads is often required when benchmarking the performance of new
bioinformatics algorithms, as results from different algorithms can only be
properly compared when tested against a common dataset where the true expected
result is known.

Short read data is stored in the standardized [FASTQ
format](https://en.wikipedia.org/wiki/FASTQ_format). This text based format
encodes information about a read, which corresponds to one DNA fragment
sequenced on the machine, in four lines as in the example below:

```
@SEQ_ID
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
+
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
```

There may be many millions of reads in a dataset, each with four lines as above.
Specifically, each read begins with an identifier line beginning with `@`,
followed by a line containing the nucleotide sequence of the read, followed by
a line with `+`, and finally with a string of characters the same length as the
read that contains quality information about the corresponding base. The quality
of each base in the corresponding read is determined by the sequencing machine,
where sometimes the instrument and software was unsure whether, for example, an
`A` it observed at one position of the read was truly an adenine in the
molecule. Since we are simulating a simple dataset we will assume the quality of
each base of each read is the maximum possible, and create the quality line with
only the character `I`.

## Problem statement

Create a simulated WGS high throughput sequencing read dataset by sampling
sequences at random from the genome.

## Baseline

### Inputs

* A fasta formatted file of a genome

### Outputs

* A fastq formatted file with 1,000,000 simulated reads of length 75

### Instructions

### Hints

## Challenge

### Inputs

### Outputs

### Hints
