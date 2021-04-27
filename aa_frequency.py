"""
The amino acids frequencies in database
"""
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from collections import Counter
import pandas as pd


db_file = r'' # fasta file of proteome database

aa_lst = []


for record in SeqIO.parse(db_file, 'fasta'):
    lst = list(str(record.seq))
    aa_lst.extend(lst)

print(f"The number of AA in db: {len(aa_lst)}")

c = Counter(aa_lst)

print(c)

print(c.most_common(10))

df = pd.DataFrame(columns=['aa','number'], data=c.most_common(25))

df['frequency'] = df['number'].map(lambda x: x/len(aa_lst))

df.to_csv(r'<name>.csv', index=False) # export results
