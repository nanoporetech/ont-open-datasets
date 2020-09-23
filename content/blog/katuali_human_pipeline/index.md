---
title: Katuali analysis pipeline for preparing human datasets
date: "2020-09-22T00:04:00.000Z"
description: "In this post we detail the open source analysis pipeline responsible for generating the GM24385 dataset."
tags:
  - datasets
  - analysis
  - GM24385
---

Our recent [GM24385 data release](/gm24385_2020.09) contains data from multiple
flowcells and analytes for both the R9.4.1 and R10.3 flowcell chemistries. The
uploaded data contains the primary sequencer output data; the full MinKNOW
output directory for the runs is included verbatim. The release seperately
contains a directory structure resulting from the application of a snakemake
analysis pipeline. Here we provide details of how this workflow was executed
and its outputs.

### Background

[Katuali](https://github.com/nanoporetech/katuali) is a set of
[Snakemake](https://snakemake.readthedocs.io/) analysis pipelines for basic
analysis of nanopore sequencing data. It can perform basic tasks such as
basecalling, alignment of reads, assembly, and evaluation and benchmarking of
such algorithms. This can be performed at scale on large compute clusters on
local or cloud infrastructure.

For the GM24385 release Katuali was used to construct secondary analyses in a
documented and reproducible fashion. As katuali is open source, it is possible
for users to reconstruct these secondary analyses for themselves from the
primary data. We have uploaded the results of these analysis to provide
benchmarking data and make available useful resources for others to perform
further analysis.

The Katuali pipeline used for the [GM24385 data release](/gm24385_2020.09)
provides four main outputs:

1. Align basecalls to reference sequence retaining all primary, secondary and
   supplementary alignments are kept
2. Filter .bam file to list of regions defined in configuration file retaining
   only primary alignments.
3. Produce read statistics from per-region .bams.
4. Repack/group source .fast5 files according to primary alignment .bams to
   produce per-region .fast5 file sets.

These outputs provide added value to the primary data, and users can extend and
adapt the katuali pipeline and configuration to calculate additional outputs.

### Katuali configuration for GM24385 release


### Pipeline data flow


### Directory listing and description 
