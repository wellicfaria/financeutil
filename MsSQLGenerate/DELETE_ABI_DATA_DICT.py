

import pandas as pd

import controllers.operationDF as op
import modelscript.hqlFile as chql

import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\MsSQLGenerate','')



xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_tabelas = pd.read_excel(xlsx, 'tabelas')

f = open(dir_path + "/filesgenerated/MSSQL/DELETE_ABI_DATA_DICT.hql", "w+")

insert_sql = "DELETE FROM IngestionDB.dbo.ABI_DATA_DICT" \
             " where Data_Lake_Object IN {} ;"


c = insert_sql.format(tuple(df_tabelas['Source_Data_Lake_Object'].tolist()))
f.write(c)

f.close()

    
