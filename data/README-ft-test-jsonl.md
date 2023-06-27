# Files ft-test-sourcefound-en-fr.jsonl and ft-test-sourcefound-fr-en.jsonl

These files contain the data used to compute the automatic counts (see score.py in the scripts directory).
The data consists of examples where a term from the PFT_ef was found on the source side.
The data is in jsonl format. Each line consists of a json object with the following fields:

* `id`: (String) The source segment identifier.
* `language`: (String) The source language (English or French).
* `source`: (String) The raw source text.
* `reference`: (String) The raw reference text.
* `mt`: (String) The MT output (postprocessed).
* `terms`: (List) A list of term pairs. Each term pair is represented by a list containing source and target strings.
* `source_tok`: (List) Tokenized source text, as a list of strings.
* `reference_tok`: (List) Tokenized reference text.
* `mt_tok`: (List) Tokenized MT output.
* `terms_tok`: (List) List of tokenized term pairs. Pairs are a list containing source and target; source and target are lists of tokenized strings.
