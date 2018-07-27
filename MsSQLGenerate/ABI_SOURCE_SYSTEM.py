from openpyxl import load_workbook
wb = load_workbook(filename='Ingestion_Tables.xlsx', read_only=True)
ws = wb['ABI_SOURCE_SYSTEM']

insert_molde = "INSERT INTO IngestionDB.dbo.ABI_SOURCE_SYSTEM \
(Src_Sys_Id, Src_Sys_Nm, Src_Sys_Batch_Nr, Src_Sys_Region_Nm, Src_Sys_Region_Type, Ins_Gmt_Ts, Upd_Gmt_Ts, Ins_Usr_Id, Upd_Usr_Id, Load_Job_Nr, Act_Fg)\
VALUES({}, '{}', {}, '{}', '{}', {}, {}, '{}', '{}', {}, '{}');"


file = open("ABI_SOURCE_SYSTEM.sql","w") 

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
            row[10].value
            ).replace("'None'", "NULL").replace("None", "NULL")
        file.write(comando_sql)
        file.write('\n')
    i+=1
    
file.close()
print("Processo Finalizado, foram escritos {} linhas no arquivo.".format(i))



    
