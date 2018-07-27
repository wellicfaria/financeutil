from openpyxl import load_workbook
wb = load_workbook(filename='Ingestion_Tables2.xlsx', read_only=True)
ws = wb['ABI_CZ_LOAD_CTL2']

insert_molde =  "INSERT INTO IngestionDB.dbo.ABI_CZ_LOAD_CTL \
(Data_Subject_CD, Source_Data_Lake_Object, Target_Data_Lake_Object, Src_Sys_Id, Source_Type, Load_Type_Code, Error_Object, Source_Temp_Object, Target_Temp_Object, Source_File_Location, Target_File_Location, Executable_Location, Source_File_Archive_Location, Temporary_Location, Rejected_File_Location, Rejected_Record_Location) \
VALUES('{}', '{}', '{}', {}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');"


file = open("ABI_CZ_LOAD_CTL.sql","w") 

i = 0
for row in ws.rows:
    if i>0:
        comando_sql = insert_molde.format(
            row[0].value,
            row[1].value,
            row[2].value,
            row[3].value,
            row[4].value,
            row[5].value,
            row[6].value,
            row[7].value,
            row[8].value,
            row[9].value,
            row[10].value,
            row[11].value,
            row[12].value,
            row[13].value,
            row[14].value,
            row[15].value
            ).replace("'None'", "NULL").replace("None", "NULL")
        file.write(comando_sql)
        file.write('\n')
    i+=1
    
file.close()
print("Processo Finalizado, foram escritos {} linhas no arquivo.".format(i))



    
