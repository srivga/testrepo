# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 15:30:13 2021

@author: gaurav.srivastava04
"""

path = 'C:\\Users\\gaurav.srivastava04\\Documents\\MARS\\15022021\\Pass Files\\644_Combined_Pass_Records.csv'

import pandas as pd
import re
import sweetviz as sv
import pandas_profiling as pp

df = pd.read_excel(path,sheet_name='644')

c = re.search(r'(\w+\s+){0,3}OZ(\w+\s+){0,3}', df['MATERIAL.DESCRIPTION'][0], re.IGNORECASE)
print(c.group(0))

b = re.findall(r'(\d+\.\d+)OZ', df['MATERIAL.DESCRIPTION'][0]) 
res = list(map(float, b))
print(res)

report = sv.analyze(df)

profile = pp.ProfileReport(df,title="TEST")


b = re.findall(r'(\w+\s+)','BRG,BALL:9MM ID,24MM OD,7MM WD',re.IGNORECASE) #{0,3}OZ(\w+\s+){0,3}
print(b.group(0))

str1 = 'BALL,BLOCK,20MM,HSR20R1SS' #'BRG,BALL:9MM ID,24MM OD,7MM WD'
p = re.compile(r"(\w+\s+)")
res = p.split(str1)
print(res)