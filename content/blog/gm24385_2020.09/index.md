---
title: GM24385 Dataset Release
date: "2020-09-22T00:00:00.000Z"
description: "Announcing the release of a GM24385 Dataset"
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

<Pullquote>
The following cell lines/DNA samples were obtained from the NIGMS Human
Genetic Cell Repository at the Coriell Institute for Medical Research:
GM24385.
</Pullquote>

***Whats included?***

The dataset comprises multiple R9.4.1 and R10.3 flowcells of multiple
separately prepared samples; each sample was run on each flowcell type.

The initial sequencer outputs are included in self container directories.
In addition derived outputs from an automated pipeline are stored
separately.

***Details concerning sample preparations***

TODO.

***Location of the data***

The data is located in an Amazon Webservice S3 bucket at:

    s3://ont-open-data/gm24385_2020.09/

See the [tutorials](/tutorials/) page for information on downloading the dataset.

***Description of available data***

TODO
