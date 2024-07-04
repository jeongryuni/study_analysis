#이번에는 DataFrame에서 조건에 해당하는 데이터를 찾는 연습을
#'KBS'에서 시청률이 30이 넘은 데이터만 확인
import pandas as pd

df = pd.read_csv('../data/broadcast.csv', index_col=0)

kbs_df = df['KBS']>30
print(df[kbs_df]['KBS'])

