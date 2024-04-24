import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)

## low 한개 가져오기
# print(iphone_df.loc['iPhone X'])

## low 여러개 가져오기 ( 리스트 형태로 가져오면 된다. )
# print(iphone_df.loc[['iPhone X','iPhone 8']]) #
# print(type(iphone_df.loc[['iPhone X','iPhone 8']])) #<class 'pandas.core.frame.DataFrame'>


## 컬럼 한개 가져오기
# print(iphone_df['Face ID'])

## 컬럼 여러개 가져오기
# print(iphone_df[['Face ID','출시일','메모리']])

# 열 슬라이싱
# print(iphone_df.loc['iPhone 8' : 'iPhone XS'])
# print(iphone_df.loc[ : 'iPhone XS'])

# 컬럼 슬라이싱
# print(iphone_df.loc[:, '메모리':'Face ID'])
print(iphone_df.loc['iPhone 7':'iPhone X', '메모리':'Face ID'])