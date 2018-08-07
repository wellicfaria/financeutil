import pandas as pd

import controllers.operationDF as op
import modelscript.hiveScriptUtil as su


import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\hiveGeneration','')


xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_tabelas = pd.read_excel(xlsx, 'tabelas')
df_colunas = pd.read_excel(xlsx, 'colunas')


set_tabelas = set(df_tabelas['Source_Data_Lake_Object'].tolist())

set_colunas = set(df_colunas['Data_Lake_Object'].unique().tolist())


f= open(dir_path+"/filesgenerated/hiveScriptDropTables.sql","w+")

for i in list(set_colunas & set_tabelas):
    f.write("\n"+su.comandDroptable('finance_hz',i))
    f.write("\n"+su.comandDroptable('finance_tmp','tmp_'+i))

f.close()