import pandas as pd

import controllers.operationDF as op
import modelscript.hiveLZScript as hivelz
import modelscript.hiveTempScript as hivehz

import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\hiveGeneration','')


xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_tabelas = pd.read_excel(xlsx, 'tabelas')
df_colunas = pd.read_excel(xlsx, 'colunas')


set_tabelas = set(df_tabelas['Source_Data_Lake_Object'].tolist())

set_colunas = set(df_colunas['Data_Lake_Object'].unique().tolist())

print("\nTabelas Mateadas OK (mapeadas em ABI_CZ_LOAD_CTL e ABI_DATA_DICT)")

f= open(dir_path+"/filesgenerated/hiveScriptManualInput.sql","w+")

for i in list(set_colunas & set_tabelas):
    colunastabela = op.getcolunasTabela(df_colunas ,i)
    localHZ= op.getLocationHZ(df_tabelas, i)
    localTMP = op.getLocationTmp(df_tabelas, i)
    f.write("\n"+hivelz.generateCreateTableComand('finance_tmp','tmp_'+i,colunastabela,localTMP))
    f.write("\n"+hivehz.generateCreateTableComand('finance_hz',i,colunastabela,localHZ))

f.close()
















