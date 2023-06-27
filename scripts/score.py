#!/usr/bin/env python3

# Check tokenized data for matches from fixed terms.

# Multilingual Text Processing / Traitement multilingue de textes
# Digital Technologies Research Centre / Centre de recherche en technologies numériques
# National Research Council Canada / Conseil national de recherches Canada
# Copyright 2023, Sa Majesté le Roi du Chef du Canada / His Majesty the King in Right of Canada

import json
import argparse
from collections import defaultdict

parser = argparse.ArgumentParser(description="Check tokenized data for matches from fixed terms.")

parser.add_argument("-i", "--inputfile", type=str, help="Input file (source).", required=True)

args=parser.parse_args()

def count_matches(ft, sent):
    if len(sent)<len(ft):
        return 0
    else:
        n = len(ft)
        return sum([ft == sent[i:i+n] for i in range(len(sent)-n+1)])

"""
Load the input data and count fixed terms.
"""
found_term_set=set()
src_found=0
ref_found=0
mt_found=0
with open(args.inputfile) as f:
    for l in f:
        j = json.loads(l.strip())
        src = j["source_tok"]
        ref = j["reference_tok"]
        mt = j["mt_tok"]
        terms = j["terms_tok"]
        for termpair in terms:
            src_term, ref_term = termpair
            found_term_set.add(tuple(src_term))
            src_matches = count_matches(src_term, src) 
            src_found += src_matches
            ref_found += min(src_matches, count_matches(ref_term, ref))
            mt_found += min(src_matches, count_matches(ref_term, mt))
            
print("Unique terms found:",len(found_term_set))
print("Count of source terms found:",src_found)
print("% source and reference match:","{:.1f}".format(100.0*ref_found/src_found))
print("% source and MT match:","{:.1f}".format(100.0*mt_found/src_found))
