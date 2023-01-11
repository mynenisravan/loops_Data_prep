# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 23:52:31 2023

@author: H283847
"""


import glob
import pandas as pd
import shutil


# assign directory
directory = 'C:\\Users\H283847\Documents\Loops-x\Output/'

# iterate over files in
# that directory
for filename in glob.iglob(f'{directory}*'):
    df_name1 = pd.read_csv(filename, sep="\t",header=None, low_memory=False)
    rows = df_name1.shape[0]
    if rows<3000:
        opath = 'C:\\Users\H283847\Documents\Loops-x\loop_3000/'
        f_name = filename.split("\\")[-1]
        print(f_name)
        opath1 = str(opath)+str(f_name)
        original = filename
        target = opath1
        shutil.copyfile(original, target)
    else:
        opath = 'C:\\Users\H283847\Documents\Loops-x\loop_17000/'
        f_name = filename.split("\\")[-1]
        print(f_name)
        opath1 = str(opath)+str(f_name)
        original = filename
        target = opath1
        shutil.copyfile(original, target)

        
        
        


