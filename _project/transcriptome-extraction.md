---
title: Predicted Transcriptome Extraction
---

## Background

The term genome refers not only to the specific DNA sequence of the molecule that
defines it but also by the individual genes contained therein. Specific parts of
a genome code for genes, whose nucleotide sequences are transcribed into RNA
molecules, many of which are then translated into proteins. The parts of a
genome that are transcribed into RNA are collectively called the *transcriptome*
which is another important attribute of a genome. The program RAST uses
bioinformatic methodology to identify the putative locations of genes within
a genome, allowing us to compute important characteristics of the organism,
including the number of genes it possesses, which specific genes and biological
functions it is capable of, etc. The RAST annotation allows us extract these gene
sequences into a new file containing only gene sequences that can be examined
separately from the genome.

## Problem statement

Create a putative transcriptome reference containing just the predicted gene
sequences in the genome using the RAST annotation coordinates.

## Baseline

Use the `gff` file produced by RAST to create a new fasta file containing just
the gene sequences from the overall genome. The coordinates in the `gff` file
are relative to the linear length of the genome, and the strand column indicates
whether the gene sequence should be reverse complemented.

### Inputs

* The `gff` file produced by RAST

### Outputs

* A fasta file with one sequence per gene, the gene ID and Name in the header
  line and nucleotide sequence extracted from the genome using the annotated
  coordinates as the sequence

### Instructions

### Hints

## Challenge

### Inputs

### Outputs

### Hints
