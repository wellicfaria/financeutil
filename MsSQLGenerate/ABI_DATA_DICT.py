

import pandas as pd


import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\MsSQLGenerate','')



xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_colunas = pd.read_excel(xlsx, 'colunas')

f = open(dir_path + "/filesgenerated/MSSQL/INSERT_ABI_DATA_DICT.sql", "w+")

insert_sql = "INSERT INTO IngestionDB.dbo.ABI_DATA_DICT" \
             " (Data_Subject_CD, Data_Lake_Object, Column_Name, Column_Data_Type, Column_Precision, Column_Key, Column_Nullable, Column_Order)" \
             " VALUES('{}', '{}', '{}', '{}', {}, '{}', '{}', {});"

for index, row in df_colunas.iterrows():
    c = insert_sql.format(row['Data_Subject_CD'],row['Data_Lake_Object'],row['Column_Name'].upper(),row['Column_Data_Type'],row['Column_Precision'],row['Column_Key'],row['Column_Nullable'],row['Column_Order']).\
        replace("'nan'",'NULL').replace('.0','').replace('nan,','NULL,')
    f.write("\n"+c)

f.close()

    
