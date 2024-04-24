import pandas as pd

df = pd.read_csv('../data/broadcast.csv', index_col=0)

# SBS와 JTBC 시청률만 확인하기
#print(df)
print(df.loc[ : ,['SBS','JTBC']])