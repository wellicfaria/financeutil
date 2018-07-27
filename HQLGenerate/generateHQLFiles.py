import pandas as pd

import controllers.operationDF as op
import modelscript.hqlFile as chql

import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\HQLGenerate','')



xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_tabelas = pd.read_excel(xlsx, 'tabelas')
df_colunas = pd.read_excel(xlsx, 'colunas')


set_tabelas = set(df_tabelas['Source_Data_Lake_Object'].tolist())

set_colunas = set(df_colunas['Data_Lake_Object'].unique().tolist())





for i in list(set_colunas & set_tabelas):
    colunastabela = op.getOnlyNamecolunasTabela(df_colunas ,i)
    f = open(dir_path + "/filesgenerated/HQL/load_"+i+'.hql', "w+")
    bd_end = 'finance_hz'
    nameTable_end = i
    coluns_temp = colunastabela
    bd_temp = 'finance_tmp'
    nameTable_temp = 'tmp_'+i

    f.write(chql.generateHQLComand(bd_end,nameTable_end,coluns_temp,bd_temp,nameTable_temp))

    f.close()
















