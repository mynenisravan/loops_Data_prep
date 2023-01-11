# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:36:36 2023

@author: H283847
"""


import glob
import pandas as pd

df = pd.DataFrame(columns=['LoopName', 'Samples'])
print (df)
# assign directory
directory = 'C:\\Users\H283847\Documents\Loops-x\Output'
 
# iterate over files in
# that directory
for filename in glob.iglob(f'{directory}/*'):
    df_name1 = pd.read_csv(filename, sep="\t",header=None, low_memory=False)
    rows = df_name1.shape[0]
    print(rows)
    df.loc[len(df.index)] = [filename,rows]

df.to_csv("C:\\Users\H283847\Documents\Loops-x\Output/row_merge.csv")