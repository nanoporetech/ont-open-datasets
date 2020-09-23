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

Katuali builds on native Snakemake functionality to provide a way of mapping
and analysis pipeline across multiple inputs with minimal fuss. How this is
achieved is describe in the katuali [documentation](https://nanoporetech.github.io/katuali/examples.html#automatic-generation-of-custom-pipeline-targets). This functionality can be used to simulataneously
process data from multiple flowcells.

A single configuration file is used to control Katuali's behaviour: what input
data it will use, what pipelines it will run, and the configuration of external
programs that it runs. The configuration file can be created from the 
provided template using the [katuali_config](https://nanoporetech.github.io/katuali/tests.html#predefined-workflows)
command.

For the purposes of the GM24385 data release this file was then customised with
details of the input datasets (the `.fast5`/`.fastq` files from MinKNOW) and a
description of the outputs that were required. The resulting files are included
in the data release under the `config` folder at:

    s3://ont-open-data/gm24385_2020.09/config/

See our [tutorials](/tutorials/) page for details on how to download these
files.

#### Setup of input directories

Katuali can be used to perform basecalling from `.fast5` files to produce
standard `.fastq` sequence files. However since basecalling was performed
during the sequencing experiments we can sidestep the basecalling procedure
and simply bootstrap the Katuali output directory with the already computed
basecalls. To do this the `setup_katuali.sh` program, located at:

    s3://ont-open-data/gm24385_2020.09/config/setup_katuali.sh

was used. This prepares a directory structure that Katuali would otherwise
produce itself whilst avoiding some expensive computations. Seperate top-level
Katuali directories were created to group flowcell data from R9.4.1 and R10.3
flowcells.

#### Important aspects of configuration file

The template configuration files need only minor customisation for the GM24385
dataset. Firstly the `DATA:` section requires specifying, for example the
R9.4.1 file contains an entries such as the following (one per flowcell):

    DATA:
        '20200914_1356_6F_PAF26223_da14221a':
            'REFERENCE': 'ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta'
            'SPLIT_FAST5_REGIONS':
                ['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20',
                'chr21', 'chr22', 'chrX', 'chrY']

The first item here is simply the name MinKNOW output directory. The
`REFERENCE` entry is a relative filepath to the genomic reference sequence
appropriate to the sample; in the case of the GM24385 dataset this is simply
the human reference genome. The final entry in the above is a list of sequence
identifies (corresponding to entries in the `REFERENCE` file) indicating how
the dataset should be separated after alignment of sequences to the reference.

The second important customisation of the template configuration file is the specification
of which output files should be created. This appears in the `PIPELINES` section:

    PIPELINES:
        all_initial: [
            # do alignments, split bams and fast5s by regions
            "{DATA}/guppy_v4.0.11_r10.3_hac_prom/align_unfiltered/{SPLIT_FAST5_REGIONS}/fast5/",
        ]
        all_add_alignment_stats: [
            # calculate alignment stats
            "{DATA}/guppy_v4.0.11_r10.3_hac_prom/align_unfiltered/calls2ref_stats.txt",
            "{DATA}/guppy_v4.0.11_r10.3_hac_prom/align_unfiltered/{SPLIT_FAST5_REGIONS}/calls2ref_stats.txt"
        ]

What these so-called "targets" cause Katuali and Snakemake to calculate is discussed below.
To have katuali perform the calculation for all items in the `DATA` section it is sufficient
to run katuali with, for example:

    katuali all_initial --configfile ../../config/r9.4.1.config

from the directory corresponding to:

    s3://ont-open-data/gm24385_2020.09/analysis/r9.4.1/

Katuali replaces the `{DATA}` and `{SPLIT_FAST5_REGIONS}` tags in the listings above with
all possible values listed in the `DATA` section of the configuration file. The resulting
matrix of targets is given to Snakemake to perform the workflows.

### Pipeline data flow and output descriptions

The filepath targets defined in the Katuali configuration files trigger
Snakemake to perform all necessary calculations required to produce the
requested files. Users interested in the Snakemake rules used to produce all
files should consult the Katuali documentation and source files
[here](https://github.com/nanoporetech/katuali/tree/master/katuali/data), which
are grouped logically according to function.

Katuali has for the most part a convention that outputs which are derived
directly from an input (or previous intermediate output) are stored in a
sub-directory of that previous input. This leads to a continued deepening of
the directory structure. A benefit of this approach is the ability to
recursively calculate new outputs of the same type without having to write
multiple rules. Downside of the approach are that it is not always easy to see
which items are the immediate outputs of an analysis stage and which are the
outputs of subsequent stages. To aid users who do not wish to examine the
Snakemake files included in Katuali, the directory listing below will aid
comprehension.

Katuali generically labels results of analysis stages using a
`<stage>_<suffix>` form, for example in the below the top level
`<guppy_v4.0.11_r10.3_hac_prom>` indicates results under this level
are results of the Guppy basecaller using the settings specified
in the Katuali configuration file under the tag `v4.0.11_r10.3_hac_prom`.
Similarly `<align_unfiltered>` indicates results from the alignment
rule generated using the `unfiltered` settings.

    .
    ├── guppy_v4.0.11_r10.3_hac_prom
    │   ├── basecalls.fastq
    │   ├── sequencing_summary.txt
    │   ├── align_unfiltered
    │   │   ├── calls2ref.bam
    │   │   ├── calls2ref.bam.bai
    │   │   ├── calls2ref_stats.txt
    │   │   ├── chr1
    │   │   │   ├── calls2ref.bam
    │   │   │   ├── calls2ref.bam.bai
    │   │   │   ├── calls2ref_stats.txt
    │   │   │   ├── fast5
    │   │   │   │   ├── batch0.fast5
    │   │   │   │   ├── batch1.fast5
    │   │   │   │   ├── ...
    │   │   │   │   └── filename_mapping.txt
    │   │   │   └── readlist.txt
    │   │   ├── chr2
    ┊	┊   ┊	...
    └── reads -> <link to MinKNOW fast5_pass directory>

(Log files have been omitted from the above listing).

**The guppy analysis stage**

The Guppy analysis stage has two outputs:

* `basecalls.fastq` - all basecalls from the basecaller in a single file.
* `sequencing_summary.txt` - per-read summary information (as produced by MinKNOW).

**Alignment analysis stage**

The alignment stage of the workflow produced the following files under the
`align_unfiltered` directory. The `unfiltered` suffix relates to the fact that
all alignments are retained, not simply the primary alignment of each read.

* `calls2ref.bam` - the alignments of reads to the supplied reference.
* `calls2ref.bam.bai` - an index file for the alignments.

An auxiliary target of the Katuali pipeline produces the following:

* `calls2ref_stats.txt` - per-read statistics calculated from the corresponding
  `calls2ref.bam`.

**Alignment filtering stage**

Having aligned the basecall data, Katuali separates the basecalls and read data
stored in the source `.fast5` data by the regions specified in the Katuali
config. A directory is produced by region, for example `chr1` in the listing
above. Under this we find:

* `calls2ref*` - files analagous to those in the `align_unfiltered` directory
  but containing only those reads with primary alignments to the given region.
* `readlist.txt` - a simple text table containing the read identifiers of the
  requisite reads.
* `fast5` - a directory containing `.fast5` files constructed from the original
MinKNOW `.fast5` files but containing only the requisite reads. The file
`filename_mapping.txt` provides a read identifier to filename mapping.


