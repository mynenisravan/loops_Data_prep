
"""
Author: Sravan Myneni
"""
import pandas as pd
import csv
import os
from sys import argv


def past_phd(input_file):
    input_path= input_file.rsplit('\\',1)
    input_path = input_path[0]
    if not os.path.exists(str(input_path)+'\\output'):
        os.makedirs(str(input_path)+'\\output')
    df = pd.read_csv(str(input_file), parse_dates=['Timestamp'], low_memory=False)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    columns = df.columns.tolist()
    df['Timestamp'] = df['Timestamp'].dt.strftime('%d-%b-%Y %H:%M:%S')
    
    for col in columns:
            if not col == 'Timestamp':
                df1 = df.loc[:,['Timestamp', str(col)]]
                new_df = df1.assign(tag=col)            
                new_df = new_df[["Timestamp","tag", col]]  
                new_df.to_csv(str(input_path)+"\\output\\"+col+".csv", index=False, quotechar='"', header=None, quoting=csv.QUOTE_NONNUMERIC)
    
input_file = "C:\\Users\\H283847\\Pictures\\test\\sag_data_raw-t.csv"
past_phd(input_file)

