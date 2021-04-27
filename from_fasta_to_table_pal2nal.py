#!/Users/igorfesenko/anaconda3/bin/python3
# -*- coding: utf-8 -*-

'''
Creating table from fasta
'''
import os
import sys
import getopt
import pandas as pd
from Bio.Seq import Seq
from Bio import SeqIO
import pandas as pd



if __name__ == "__main__":
   
    unixOptions = "d:"  
    gnuOptions = ["dir="]
    # Получаем строку входных параметров
    fullCmdArguments = sys.argv
    argumentList = fullCmdArguments[1:]

    try:  
        arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
    except getopt.error as err:  
        print (str(err))
        sys.exit(2)      

    # reading arguments
    directory = '' 
    
    for currentArgument, currentValue in arguments:  
        if currentArgument in ("-d", "--dir"):
            directory = currentValue   

    #reading fasts files in directory                               
    
    names = [n for n in os.listdir(path=f"{directory}") if n.endswith('.fasta')]


    # creating table
    df = pd.DataFrame()


    # fasta files parsing
    cnt=1
    for name in names:
        tmp_fasta =[]
        for record in SeqIO.parse(name, 'fasta'):
            tmp_fasta.append([record.id, record.seq])
        df.join(pd.DataFrame(data=tmp_fasta, columns=[f"ID_{cnt}",f"Seq_{cnt}"]))
        cnt+=1

    df.to_csv(f"{directory}/table.csv", index=False)