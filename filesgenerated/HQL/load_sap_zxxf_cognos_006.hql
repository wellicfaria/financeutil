Insert into table finance_hz.sap_zxxf_cognos_006 partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  MANDT7, PRCTR1, MVGR1, ZZDIM1,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_sap_zxxf_cognos_006