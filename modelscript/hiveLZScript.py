

comand_create_table = \
    "CREATE EXTERNAL TABLE IF NOT EXISTS  {}.{}(" \
    "{}" \
    ")" \
    "ROW FORMAT DELIMITED" \
    " FIELDS TERMINATED BY '\\043' " \
    " STORED AS INPUTFORMAT" \
    " 'org.apache.hadoop.mapred.TextInputFormat'" \
    " OUTPUTFORMAT" \
    " 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'" \
    " LOCATION" \
    " 'adl://edhdatalakestorewe.azuredatalakestore.net{}'" \
    " TBLPROPERTIES (" \
    " 'last_modified_by'='haadmin'," \
    " 'last_modified_time'='1532031952'," \
    " 'numFiles'='10'," \
    " 'totalSize'='12010'," \
    " 'transient_lastDdlTime'='1532098273');"




def generateCreateTableComand(bdhive,nametable,coluns,location):

    return  comand_create_table.format(bdhive,nametable,coluns,location)

