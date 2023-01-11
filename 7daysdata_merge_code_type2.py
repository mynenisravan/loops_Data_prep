# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 13:41:03 2022

@author: H283847
"""

import pandas as pd

df = pd.DataFrame()
LL = 14
HH = 15
for x in range (LL,HH+1):
    path = "C:\\Users\\H283847\\Desktop\\SR2HCU\\SR2HCU\SR2HCU_Inputfile"
    try:
        if x==LL: 
      
            num = str(x)
            ext = ".txt"
            input_file = path+num+ext
            df_name1 = pd.read_csv(input_file, sep="\t",header=None, low_memory=False)
            df = df.append(df_name1[:])
            
        else:
            
            num = str(x)
            ext = ".txt"
            input_file = path+num+ext
            df_name1 = pd.read_csv(input_file, sep="\t",header=None, low_memory=False)
            df = df.append(df_name1[2:])
            
    except FileNotFoundError as e:
        print("FileNotFoundError successfully handled\n" f"{e}")

    
df.to_csv("C:\\Users\\H283847\\Desktop\\SR2HCU\\SR2HCU\SR2HCU_Inputfile_merge.csv", header=None)
