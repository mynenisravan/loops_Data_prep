# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:46:47 2023

@author: H283847
"""

import glob
 
# assign directory
directory = 'C:\\Users\H283847\Documents\Loops-x\Output'
 
# iterate over files in
# that directory
for filename in glob.iglob(f'{directory}/*'):
    print(filename)