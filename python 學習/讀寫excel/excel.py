# * -*- coding: utf-8 -*-
import pandas as pd
MKT = 'MKT1.xlsx'
A02 = 'A02.xlsx'

df = pd.read_excel(MKT, sheet_name='MKT1')

for i in df['产品']:
    if i == 'A02':
        df.loc[df['产品'] == 'A02'].to_excel(i+'.xlsx', sheet_name=i)
        # print(df.loc[df['产品'] == 'A02'])
