Insert into table finance_hz.sap_fornecimento partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  MANDT, NUM_CONTROL, WERKS, NUM_CONT, MJAHR, BWART, MATNR, CHARG, SHKZG, BWTAR, MENGE, MEINS, KOSTL, BUDAT_MKPF, CPUDT_MKPF, XBLNR_MKPF, Z_DATA_SAP, Z_HORA_SAP, Z_LEIT_ETL, Z_HORA_LEIT_ETL, Z_RET_ETL, Z_HORA_RET_ETL, Z_CONF_LEI,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_sap_fornecimento