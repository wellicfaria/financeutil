

import pandas as pd


import os
dir_path = os.path.dirname(os.path.realpath(__file__)).replace('\MsSQLGenerate','')



xlsx = pd.ExcelFile(dir_path+'/files/manualinput.xlsx')
df_tabelas = pd.read_excel(xlsx, 'tabelas')

f = open(dir_path + "/filesgenerated/MSSQL/INSERT_CZ_LOAD_CTL.sql", "w+")

insert_sql = "INSERT INTO IngestionDB.dbo.ABI_CZ_LOAD_CTL" \
             "(Data_Subject_CD, Source_Data_Lake_Object, Target_Data_Lake_Object, Src_Sys_Id, Source_Type, Load_Type_Code, Error_Object, Source_Temp_Object, Target_Temp_Object, Source_File_Location, Target_File_Location, Executable_Location, Source_File_Archive_Location, Temporary_Location, Rejected_File_Location, Rejected_Record_Location)" \
             "VALUES('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"

for index, row in df_tabelas.iterrows():
    c = insert_sql.format(row['Data_Subject_CD'],row['Source_Data_Lake_Object'],row['Target_Data_Lake_Object'],row['Source_System_ID'],row['Source_Type'],row['Load_Type_Code'],row['Error_Object'],row['Source_Temp_Object'],row['Target_Temp_Object'],row['Source_File_Location'],row['Target_File_Location'],row['Executable_Location'],row['Source_File_Archive_Location'],row['Temporary_Location'],row['Rejected_File_Location'],row['Rejected_Record_Location']).\
        replace("'nan'",'NULL').replace('.0','').replace('nan,','NULL,')
    f.write("\n"+c)

f.close()
