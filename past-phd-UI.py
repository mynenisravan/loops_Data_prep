# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 17:00:33 2022

@author: H283847
"""
import pandas as pd
import csv
import os
from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Source File path ')
        self.t1=Entry(bd=2, width=75)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.b1=Button(win, text='Generate', command = self.past_phd)
        self.b1.place(x=100, y=150)
    

    def past_phd(self):
        input_file=str(self.t1.get().strip('"'))
        input_path= input_file.rsplit('\\',1)
        input_path = input_path[0]
        if not os.path.exists(str(input_path)+'\\output'):
            os.makedirs(str(input_path)+'\\output')
        df = pd.read_csv(str(input_file), parse_dates=['Timestamp'])
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        columns = df.columns.tolist()
        df['Timestamp'] = df['Timestamp'].dt.strftime('%d-%b-%Y %H:%M:%S')
        
        for col in columns:
                if not col == 'Timestamp':
                    df1 = df.loc[:,['Timestamp', str(col)]]
                    new_df = df1.assign(tag=col)            
                    new_df = new_df[["Timestamp","tag", col]]  
                    new_df.to_csv(str(input_path)+"\\output\\"+col+".csv", index=False, quotechar='"', header=None, quoting=csv.QUOTE_NONNUMERIC)
        self.lbl3=Label(text='The files are generated at '+ str(input_path)+"\\output\\")
        self.lbl3.place(x=100, y=200)

window=Tk()
mywin=MyWindow(window)
window.title('Past data files into PHD')
window.geometry("800x300+10+10")
window.mainloop()
