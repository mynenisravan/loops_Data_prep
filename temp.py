# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

df = pd.read_csv("C:\\Users\\H283847\\Desktop\\Temp\\SDM1.csv")

columns = df.columns.tolist()

type(columns)



for col in columns:
        if not col == 'Timestamp':
            df1 = df.loc[:,['Timestamp', str(col)]]
            new_df = df1.assign(tag=col)
            new_df = new_df[["Timestamp","tag", col]]
            new_df.to_csv("C:\\Users\\H283847\\Desktop\\Temp\\output\\"+col+" .csv", header=False, index = False)

