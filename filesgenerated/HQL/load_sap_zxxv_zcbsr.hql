Insert into table finance_hz.sap_zxxv_zcbsr partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  MANDT, NUM_CONTROL, WERKS, NUM_CONT, KOKRS, GJAHR, MONAT, MATNR, BWTAR, ZZCME, ZBWMP, KSTAR, ZZGRP, ZZSGR, ZWERKS, ZZEPA, ZZVEPA, ZZQCP, ZZCCM, ZZQRFA, ZZCRFA, ZZCMU, ZZQMU, Z_DATA_SAP, Z_HORA_SAP, Z_LEIT_ETL, Z_HORA_LEIT_ETL, Z_RET_ETL, Z_HORA_RET_ETL, Z_CONF_LEI,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_sap_zxxv_zcbsr