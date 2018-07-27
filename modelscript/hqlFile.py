

comand_hql= 'Insert into table {}.{} partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select {},context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from {}.{}'


def generateHQLComand(bd_end,nameTable_end,coluns_temp,bd_temp,nameTable_temp):
    return  comand_hql.format(bd_end,nameTable_end,coluns_temp,bd_temp,nameTable_temp)