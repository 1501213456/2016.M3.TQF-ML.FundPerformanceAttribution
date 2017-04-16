import numpy as np
import pandas as pd
from datetime import datetime,date,timedelta
benchmark=pd.read_csv('Benchmark_Index.csv',index_col=0)
activefunds=pd.read_csv('Target_Active_Funds.csv',index_col=0)
df_benchmark=benchmark/benchmark.shift(1)-1
df_benchmark=df_benchmark[1:]
df_benchmark=df_benchmark[df_benchmark.index<'2017/1/1']
df_activefunds=activefunds/activefunds.shift(1)-1
df_activefunds=df_activefunds[1:]
df_activefunds=df_activefunds[df_activefunds.index<'2017/1/1']
benchmark_list=df_benchmark.columns.tolist()
activefunds_list=df_activefunds.columns.tolist()
print(df_activefunds)