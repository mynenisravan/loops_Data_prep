# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 16:59:46 2022

@author: H283847
"""
import os  
day=5
path = "C:\\Users\\H283847\\Downloads\\CPMAPC\\"+str(day)+"\\Input"
files = os.listdir(path)

        
for index, file in enumerate(files):
     name = file.split(".")[0]
     name1 = str(name)+"_"+str(day)
     os.rename(os.path.join(path, file),os.path.join(path,''.join([str(name1),'.txt'])))
    #os.rename(os.path.join(path, file),os.path.join(path,''.join(['3_',str(file)])))