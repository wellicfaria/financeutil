
#PEGA PARA CRIAR O COMANDO HIVE, NAO USA PARA O MSSQL
def getcolunasTabela(df_colunas,name_table):

    df = df_colunas.loc[df_colunas['Data_Lake_Object']==name_table]

    colunas = df['Column_Name'].tolist()
    tipos_colunas = df['Column_Data_Type'].tolist()

    resp = ""
    for i in range(0,len(colunas)):
       aux = " {} {},".format(colunas[i],tipos_colunas[i].replace('long','bigint').replace('date','string'))
       resp+=aux

    return resp[0:-1]

def getLocationHZ(df_tabelas,name_table):
    df = df_tabelas.loc[df_tabelas['Source_Data_Lake_Object'] == name_table]
    location=df['Target_File_Location'].tolist()[0]
    return location

def getLocationTmp(df_tabelas,name_table):
    df = df_tabelas.loc[df_tabelas['Source_Data_Lake_Object'] == name_table]
    location=df['Temporary_Location'].tolist()[0]
    return location

def getOnlyNamecolunasTabela(df_colunas,name_table):

    df = df_colunas.loc[df_colunas['Data_Lake_Object']==name_table]

    colunas = df['Column_Name'].tolist()

    resp = ""
    for i in range(0,len(colunas)):
       aux = " {},".format(colunas[i])
       resp+=aux

    return resp[0:-1]

