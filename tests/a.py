import pandas as pd
from gene_signature_survival import signature_surv

#inputs
Pos = ['MMP1', 'QSOX1', 'OXTR', ]
Neg = ['MSX1', 'ELN', 'PMP22']

dir = r'tests'
df_expression = None
df_clinical = None
event = 'RFS_Status'
time = 'RFS_time_Days'
time_units = 'Days'
score_name = 'EMT'


signature_surv(df_expression, df_clinical, time, time_units, event, dir, score_name, Pos, Neg)