import pandas as pd
df = pd.read_csv('../data/broadcast.csv', index_col=0)

# 2016년도에 KBS방송국의 시청률을 찾아보기
print(df.loc[2016, 'KBS'])