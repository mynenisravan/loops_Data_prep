# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:46:47 2023

@author: H283847
"""

import glob
import pandas as pd

df = pd.DataFrame()
 
# assign directory
directory = 'C:\\Users\H283847\Documents\Loops-x\Output - Copy'
 
# iterate over files in
# that directory
for filename in glob.iglob(f'{directory}/*'):
    df_name1 = pd.read_csv(filename, sep="\t",header=None, low_memory=False)
    df= pd.concat([df, df_name1], axis=1)
    print(df)

df.to_csv("C:\\Users\H283847\Documents\Loops-x\Output - Copy\SR2HCU_Inputfile_merge.csv", header=None)