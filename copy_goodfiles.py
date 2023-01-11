# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 16:54:29 2023

@author: H283847
"""

import pandas as pd
import shutil

df = pd.read_csv("C:\\Users\\H283847\Documents\Loops-x\OneDrive_1_7-26-2022\good_loops.csv")
print(df)
good_loops_list = df["Loop name"]
ipath = "C:\\Users\\H283847\\Documents\\Loops-x\\Input\\"
opath = "C:\\Users\\H283847\\Documents\\Loops-x\Output\\"
for name in good_loops_list:
    
    ipath1 = str(ipath)+ str(name)+".txt"
    opath1 = str(opath)+ str(name)+".txt"
    
    original = ipath1
    target = opath1
    shutil.copyfile(original, target)


# =============================================================================
# 
# 
# import os
# import shutil
# 
# source_folder = r"E:\demos\files\reports\\"
# destination_folder = r"E:\demos\files\account\\"
# 
# # fetch all files
# for file_name in os.listdir(source_folder):
#     # construct full file path
#     source = source_folder + file_name
#     destination = destination_folder + file_name
#     # copy only files
#     if os.path.isfile(source):
#         shutil.copy(source, destination)
#         print('copied', file_name)
# =============================================================================
