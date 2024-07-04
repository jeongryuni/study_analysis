import pandas as pd

df = pd.read_csv('../data/broadcast.csv', index_col=0)

# SBS가 TV CHOSUN보다 더 시청률이 낮았던 시기의 데이터
lose_df = df['SBS'] < df['TV CHOSUN']

print(df.loc[lose_df, ['SBS','TV CHOSUN']])
print(df[lose_df][['SBS', 'TV CHOSUN']])