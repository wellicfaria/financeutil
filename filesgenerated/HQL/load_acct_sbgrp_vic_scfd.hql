Insert into table finance_hz.acct_sbgrp_vic_scfd partition(Src_Sys_Region_Nm = context_src_sys_region_nm,Partition_Date = context_current_date) select  cd_country, cd_sbgrp_vic, cd_scfd_account,context_src_sys_id,context_ins_usr_id,context_upd_usr_id,context_ins_gmt_ts,context_upd_gmt_ts,context_load_job_nr,context_act_fg from finance_tmp.tmp_acct_sbgrp_vic_scfd