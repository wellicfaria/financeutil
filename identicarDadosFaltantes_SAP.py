import pandas as pd

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


xlsx_tabelas = pd.ExcelFile(dir_path+'/files/tabelas.xlsx')
df_tabelas = pd.read_excel(xlsx_tabelas, 'tabelas')

xlsx_colunas = pd.ExcelFile(dir_path+'/files/colunas.xlsx')
df_colunas = pd.read_excel(xlsx_colunas, 'colunas')

print("\nTabelas Mapeadas em ABI_CZ_LOAD_CTL:")
set_tabelas = set(df_tabelas['Source_Data_Lake_Object'].tolist())
for i in list(set_tabelas):
    print(i)

print("\nTabelas com colunas Mapeadas em ABI_DATA_DICT:")
set_colunas = set(df_colunas['Data_Lake_Object'].unique().tolist())
for i in list(set_colunas):
    print(i)

print("\nTabelas Mateadas OK (mapeadas em ABI_CZ_LOAD_CTL e ABI_DATA_DICT)")
for i in list(set_colunas & set_tabelas):
    print(i)


print("\nTabelas Faltantes em ABI_DATA_DICT")
for i in list(set_tabelas - set_colunas):
    print(i)


print("\nTabelas Faltantes em ABI_CZ_LOAD_CTL")
for i in list(set_colunas - set_tabelas):
    print(i)







