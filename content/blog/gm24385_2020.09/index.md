---
title: GM24385 Dataset Release
date: "2020-09-22T00:03:00.000Z"
description: "Announcing the release of a GM24385 (GIAB HG002) dataset."
tags:
  - datasets
  - human cell-line
  - R10.3
  - R9.4.1
---

We are happy to annouce the release of a Nanopore sequencing dataset
of the Genome in a Bottle sample GM24385.

Multiple PromethION flowcells using both the R9.4.1 and R10.3 nanopores.
The direct sequencer output is included, raw signal data stored in
.fast5 files and basecalled data in .fastq file. Additional secondary
analyses are included, notably alignments of sequence data to the
reference genome are provided along with statistics derived from these.

*The following cell lines/DNA samples were obtained from the NIGMS Human
Genetic Cell Repository at the Coriell Institute for Medical Research:
GM24385.*


***Whats included?***

The dataset comprises multiple R9.4.1 and R10.3 flowcells of multiple
separately prepared samples; each sample was run on each flowcell type.

The initial sequencer outputs are included in self container directories.
In addition derived outputs from an automated pipeline are stored
separately.

***Details concerning sample preparations***

- High molecular weight DNA from GM24385 lymphoblastoid cells was prepared by 
  Evotec.
- Circulomics Short Read Eliminator XL protocol was used to deplete DNA
  fragments < 40kb in length.
- (optional) Megaruptor was used to shear DNA to obtain DNA fragments with
  an approximate N50 of 30kb.
- DNA was end repaired and dA tailed prior to LSK based library preparation.
- DNA sequencing was performed using PromethION device.

The following cell line samples were obtained from the NIGMS Human Genetic Cell
Repository at the Coriell Institute for Medical Research: GM24385

***Location of the data***

The data is located in an Amazon Webservice S3 bucket at:

    s3://ont-open-data/gm24385_2020.09/

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
