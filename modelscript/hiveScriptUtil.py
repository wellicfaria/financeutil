

comando_dropTable = "DROP TABLE IF EXISTS {}.{};"

def comandDroptable(bd_hive,name_table):
    return comando_dropTable.format(bd_hive,name_table)