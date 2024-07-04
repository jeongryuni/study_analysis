import pandas as pd

df = pd.read_csv('../data/broadcast.csv', index_col=0)

# DataFrame에서 연속된 여러줄 찾기
# 방송사는 'KBS'에서 'SBS'까지, 연도는 2012년부터 2017년까지의 시청률만 확인

print(df.loc[2012:2017, 'KBS':'SBS'])