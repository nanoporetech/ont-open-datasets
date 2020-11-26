---
title: November 2020 GM24385 Dataset Release
date: "2020-11-26T11:38:00.000Z"
description: "An updated GM24385 (GIAB HG002) dataset including data from the Ultra Long Kit (ULK)"
tags:
  - datasets
  - human cell-line
  - R9.4.1
---

We are happy to annouce an updated release of nanopore sequencing
of the Genome in a Bottle sample GM24385.

Multiple PromethION flowcells using R9.4.1 nanopores were used, along with two
different sample preparation methods. The direct sequencer output is included,
raw signal data stored in .fast5 files and basecalled data in .fastq file.
Additional secondary analyses are included, notably alignments of sequence data
to the reference genome are provided along with statistics derived from these.

Highlights of the dataset include:

- Demonstration of >200Gb from improved flowcell reliabilit,
- Inclusion of data from the new Ultra Long Kit.

A brief report comparing the current release to the previous can be found
[here](/misc/gm24385_compare.html). 


***Whats included?***

The dataset comprises data from multiple R9.4.1 flowcells.

The initial sequencer outputs are included in self container directories.
In addition derived outputs from an automated pipeline are stored
separately.


***Details concerning sample preparations***

Below is described briefly the method of analyte preparation. Standard, published
protocols were followed with no intentional deviation.

*The following cell line samples were obtained from the NIGMS Human Genetic Cell
Repository at the Coriell Institute for Medical Research: GM24385*

The extracted DNA was subjected to one of two protocols. The first protocol
entailed:

- High molecular weight DNA from GM24385 lymphoblastoid cells was prepared by 
  [Evotec](https://www.evotec.com/en).
- [Circulomics Short Read Eliminator XL](https://www.circulomics.com/store/Short-Read-Eliminator-XL-p138401730)
  protocol was used to deplete DNA fragments < 40kb in length.
- DNA was end repaired and dA tailed prior to LSK based library preparation.

The second protocol used the new Ultralong Sequencing Kit (ULK).

In both cases sequencing was performed using PromethION device.

The dataset comprises multiple flowcells for each pore:

| Treatmeant       | Flowcells          |
|:----------------:|:------------------:|
|        SRE       | PAG07162, PAG07165 |
|        ULK       | PAG07506           |


***Location of the data***

The data is located in an Amazon Webservice S3 bucket at:

    s3://ont-open-data/gm24385_2020.11/

See the [tutorials](/tutorials/) page for information on downloading the dataset.


***Description of available data***

The uploaded dataset has been prepared using a snakemake pipeline to:

1. Align basecalls to reference sequence. All primary, secondary and
supplementary alignments are kept
2. Filter .bam file to list of regions defined in configuration file
retaining only primary alignments.
3. Produce read statistics from per-region .bams.
4. Repack/group source .fast5 files according to primary alignment .bams
to produce per-region .fast5 file sets.

For more details see our [post](/katuali_human_pipeline/) detailing the
pipeline and its outputs.

