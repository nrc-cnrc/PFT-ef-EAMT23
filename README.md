# English-French Parliamentary Fixed Terms for EAMT 2023

## Overview

This repository contains code and data for replicating experiments in the paper Terminology in Neural Machine Translation: A Case Study of the Canadian Hansard by Rebecca Knowles, Samuel Larkin, Marc Tessier, and Michel Simard, published at EAMT 2023.

## Data

Within the `data/` directory, you will find the following files:

- `apos.txt`: This file contains the three apostrophe types that were standardized to a single type for our experiments.

- `pft-enfr.tsv`: This tab-separated file contains the terms from the English to French term bank used in our experiments. The first column is the term in English and the second column is the term translation in French.

- `README-ft-test-jsonl.md`: A readme explaining the `ft-test-sourcefound-*.jsonl` files in more detail:

  - `ft-test-sourcefound-en-fr.jsonl`: This is the main data file for most of the work described in the surface analysis portion of the paper, using text that was originally in English and translated to French. This file contains one json entry per line, including the source, reference, machine translation, and terms, along with all of these in their lowercased, apostrophe-normalized, and tokenized form.

  - `ft-test-sourcefound-fr-en.jsonl`: This version contains text that was originally produced in French and translated to English; it is briefly discussed in the surface analysis section.

- `README-ft-test-annotations.md`: A readme explaining the `ft-test-annotations.tsv` file in more detail:

  - `ft-test-annotations.tsv`: A tab-separated file containing the human-annotated test data.

## Scripts

Within the `scripts/` directory, you will find the file `score.py`: This file reproduces the FT-test lines of table 3. You can run it as:

```bash
python3 score.py -i ../data/ft-test-sourcefound-en-fr.jsonl
```

and

```bash
python3 score.py -i ../data/ft-test-sourcefound-fr-en.jsonl
```

## Copyright

The annotated data is reproduced in accordance with the [Speaker’s Permission Regarding the Reproduction of the Proceedings of the House of Commons and its Committees](https://www.ourcommons.ca/en/important-notices#SpeakersPermission); the House of Commons data has been made publicly available for unofficial, non-commercial reproduction, while copyrights are still reserved by the House of Commons.

The code copyright is as follows:

```text
Multilingual Text Processing / Traitement multilingue de textes
Digital Technologies Research Centre / Centre de recherche en technologies numériques
National Research Council Canada / Conseil national de recherches Canada
Copyright (C) 2023 Sa Majesté le Roi du Chef du Canada / His Majesty the King in Right of Canada
```

## Licence

Published under the CC BY-NC 4.0 licence (see [LICENCE](LICENCE) or visit the [website](http://creativecommons.org/licenses/by-nc/4.0/) to learn more).

## Citing this work

If you use this code or annotations, you may wish to cite:

```bibtex
@InProceedings{knowles-etal:2023:EAMT,
  author         = {Knowles, Rebecca and Larkin, Samuel and Tessier, Marc and Simard, Michel},
  title          = {Terminology in Neural Machine Translation: A Case Study of the {Canadian Hansard}},
  booktitle      = {Proceedings of the 24th Annual Conference of the European Association for Machine Translation},
  month          = {June},
  year           = {2023},
  address        = {Tampere, Finland},
  publisher      = {European Association for Machine Translation},
  pages          = {481-488},
  url            = {https://events.tuni.fi/uploads/2023/06/11678752-proceedings-eamt2023.pdf}
}
```
