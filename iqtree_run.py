#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Running IQ-TREE
'''

import os
import sys
import getopt
import pandas as pd
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO

if __name__ == "__main__":

    # reading files
    cwd = os.getcwd()
    names = [n for n in os.listdir() if n.startswith('PROT')]


    # running mafft
    for n in names:
        print(n)
        os.system(f"iqtree -s {n} -quiet > log.txt")

