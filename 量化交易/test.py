import numpy as np
import pandas as pd
import tushare as ts

####下载数据
# df = ts.get_hist_data('399300',start='2019-01-01',end='2019-12-31') #一次性获取全部日k线数据
# print(df)
# print(type(df))
# df.to_csv('399300.csv')


####读取数据
df = pd.read_csv('399300.csv')

df["signal"] = np.NaN
# print(df)
# print(type(df))
#
# print(df['p_change']<-5)

# df['p_change']
#
# print(df['p_change']<-2)
#
# a =  df[df['p_change']<-2]
# print(a)



for i in (df[df['p_change']<-2]).index:
    print(i)
    df['signal'][i]=1

print(df)
print(type(df))
df.to_csv('ok.csv')