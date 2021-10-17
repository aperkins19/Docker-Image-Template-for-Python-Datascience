import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from seaborn.matrix import heatmap


from Bio import SeqIO

def print_all_df(df):
    """ function to print a full dataframe """
    
    # Permanently changes the pandas settings
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', -1)

    # All dataframes hereafter reflect these changes.
    print(df)

    print('**RESET_OPTIONS**')

    # Resets the options
    pd.reset_option('all')

### PLACEHOLDER CODE
    
#navigation
path = "genbank_files"
os.chdir(path)

cols = ['ID', 'Name', 'Sequence', 'Length']
PURE_System = pd.DataFrame(columns = cols)

for i, filename in enumerate(os.listdir(os.getcwd())):
    record = SeqIO.to_dict(SeqIO.parse(filename, "genbank"))

    for key , value in record.items():
        PURE_System.loc[len(PURE_System.index)] = [i, key, str(value.seq), len(value.seq)]


print("PURE_System")

### PLACEHOLDER CODE
