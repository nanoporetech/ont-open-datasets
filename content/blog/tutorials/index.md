---
title: ONT Open Datasets Tutorials
date: "2020-09-22T00:01:00.000Z"
description: "Introduction to obtaining and using the available datasets."
tags:
 - tutorials
 - downloads
---

Below you will find helpful information and links out to tutorials for
datasets within the Open Datasets project.

***How can I access the data?***

All the data is stored under in an Amazon Web Services S3 bucket:

    s3://ont-open-data

This public has public permissions for anyone to obtain the data
without requiring login credentials. To download the data we
recommend using the [AWS command line interface](https://aws.amazon.com/cli/).
With the CLI installed listing the datasets can be performed with:

    aws s3 ls --no-sign-request s3://ont-open-data/

There will be a subdirectory per dataset release. Inside each dataset
will be contained a README.md file with brief details. This website
will contain additional details for each dataset.

To download datasets or extracts thereof we recommend using the `sync`
command:

    aws s3 sync --no-sign-request s3://ont-open-data/gm24385_2020.09 gm24385_2020.09

Datasets may be added to or amended over time so using `sync` can be
used with a previously fetch copy to update with the latest changes
and additions.

***Running workflows using ONT's EPI2ME platform***

Oxford Nanopore's [EPI2ME](https://epi2me.nanoporetech.com/)
platform includes several workflows for analysing
genomics datasets in the cloud with Amazon Web Services, reducing the
computational burden on the users local compute infrastructure.
For example, the [FASTQ Human Alignment GRCh38](https://community.nanoporetech.com/protocols/epi2me/v/mte_1014_v1_revba_11apr2016/human-alignment-grch38)
can be used to perform alignment of nanopore sequencing reads to 
the human reference genome to obtain industry standard BAM file outputs.

***How can I recreate the analysis directories?***

With each dataset release we will include details of how the analysis
directories were constructed from the primary inputs. For example for
the [GM24385](/gm24385_2020.09) dataset release [this page](/katuali_human_pipeline)
contains details of the Snakemake pipeline used.
