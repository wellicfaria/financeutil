Insert into table finance_hz.acct_scfd partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  cd_country, cd_scfd_account, account_1, account_2, account_3, account_4, account_5, abv_unit_msrmnt, raw, pro_memorie, p_l, level,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_acct_scfd