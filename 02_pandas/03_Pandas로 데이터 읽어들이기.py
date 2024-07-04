import pandas as pd

iphone_df = pd.read_csv('iphone.csv', index_col=0) # 0번째 인덱스의 컬럼
# 헤더가 없는 경우
# iphone_df = pd.read_csv('iphone.csv, header = None')

print(iphone_df)
print(type(iphone_df))
