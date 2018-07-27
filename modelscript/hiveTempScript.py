

comand_create_table = "CREATE EXTERNAL TABLE IF NOT EXISTS {}.{}(" \
             "{}," \
             " src_sys_id string," \
             " ins_usr_id string, " \
             " upd_usr_id string, " \
             " ins_gmt_ts string, " \
             " upd_gmt_ts string, " \
             " load_job_nr string," \
             " act_fg string" \
             " )" \
             " PARTITIONED BY ( " \
             " src_sys_region_nm string, " \
             " partition_date string)" \
             " ROW FORMAT SERDE " \
             " 'org.apache.hadoop.hive.ql.io.orc.OrcSerde' " \
             " STORED AS INPUTFORMAT " \
             " 'org.apache.hadoop.hive.ql.io.orc.OrcInputFormat' " \
             " OUTPUTFORMAT " \
             " 'org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat'" \
             " LOCATION" \
             " 'adl://edhdatalakestorewe.azuredatalakestore.net{}'" \
             " TBLPROPERTIES (" \
             " 'skip.header.line.count'='1', " \
             " 'last_modified_by'='haadmin', " \
             " 'last_modified_time'='1532031952', " \
             " 'numFiles'='10', " \
             " 'totalSize'='12010', " \
             " 'transient_lastDdlTime'='1532098273');"

def generateCreateTableComand(bdhive,nametable,coluns,location):

    return  comand_create_table.format(bdhive,nametable,coluns,location)