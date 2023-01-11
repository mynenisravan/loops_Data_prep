# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:41:03 2022

@author: H283847
"""

import pandas as pd

df = pd.DataFrame()
LL = 1
HH = 3
for x in range (LL,HH+1):
    path = "C:\\Users\\H283847\\Downloads\\CPMAPC_2\\CPMAPC\\B1301_CTL\B1301_CTL"
    try:
        if x==LL: 
            # path = "C:\\Users\H283847\Documents\OMAN\HCU\Input\HCU_"
            num = '_'+str(x)
            ext = ".txt"
            input_file = path+num+ext
            df_name1 = pd.read_csv(input_file, sep="\t",header=None, low_memory=False)
            df = df.append(df_name1[:])
            
        else:
            # path = "C:\\Users\H283847\Documents\OMAN\HCU\Input\HCU_"
            num = '_'+str(x)
            ext = ".txt"
            input_file = path+num+ext
            df_name1 = pd.read_csv(input_file, sep="\t",header=None, low_memory=False)
            df = df.append(df_name1[2:])
    except FileNotFoundError as e:
        print("FileNotFoundError successfully handled\n" f"{e}")

    
df.to_csv("C:\\Users\H283847\Downloads\CPMAPC_2\CPMAPC\B1301_CTL\merge.csv", header=None)
