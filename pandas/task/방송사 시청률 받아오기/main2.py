import pandas as pd
df = pd.read_csv('../data/broadcast.csv', index_col=0)

# JTBC의 시청률을 확인하기
print(df.loc[:, 'JTBC'])