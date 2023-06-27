# File ft-test-annotations.tsv

This file contains the manually annotated examples from the "FT-test" sample.
We omit the examples with alignment errors.
The data is tab-separated-values (TSV) format.
The first line is a header. Fields are as follows:

* `ID`: (String) The source segment identifier. Note that there are two entries for each ID: one for the reference (human) translation and one for the machine translation. See `Translation_type` below.
* `Text_source`: (String) The source segment text
* `Text_translation`: (String) The translation text
* `Translation_type`: (String) The origin of the translation, either `reference` or `MT`
* `Term_source`: (String) The source-language term that is the focus of the annotation
* `Term_translation`: (String) The target-language translation of `Term_source`, as prescribed in the *PFT_ef*
* `Source_match_total`: (Integer) The total number of matches of `Term_source` in `Text_source`
* `Target_match_total`: (Integer) The total number of matches of `Term_translation` in `Text_translation`
* `Source_match_number`: (Integer) The match of `Term_source` that is the focus of the annotation (starts at 1)
* `Target_match_present`: (Boolean) Whether there is an occurrence of `Term_translation` in `Text_translation` that matches the `Term_source` occurrence that is the focus of the annotation
* `Term_Translation_good`: (Boolean) Whether the `Term_source` occurrence that is the focus of the annotation is correctly translated in `Text_translation`
