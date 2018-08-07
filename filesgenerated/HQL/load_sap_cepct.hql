Insert into table finance_hz.sap_cepct partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  MANDT12, SPRAS1, PRCTR3, DATBI1, KOKRS1, KTEXT, LTEXT, Z_DATA_SAP1, Z_HORA_SAP1, Z_LEIT_ETL1, Z_HORA_LEIT_ETL1, Z_RET_ETL1, Z_HORA_RET_ETL1, Z_CONFLEI1, Z_CDCHGID1,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_sap_cepct