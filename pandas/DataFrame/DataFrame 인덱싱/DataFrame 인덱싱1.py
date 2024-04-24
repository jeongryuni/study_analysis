import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)
#print(iphone_df) # 출력

## 아이폰8의 메모리만 불러오기
#print(iphone_df.loc['iPhone 8', '메모리']) #2GB
#print(iphone_df.loc['iPhone 8', '가격']) # 가격이라는 컬럼이 없기때문에 오류가 남

## 아이폰X의 모든 컬럼 불러오기
#print(iphone_df.loc['iPhone X', :])

# Series는 판다스의 1차원 자료형
#print(type(iphone_df.loc['iPhone X'])) #<class 'pandas.core.series.Series'>

## 아이폰의 출시일 모두 불러오기
#print(iphone_df.loc[:,'출시일'])
#print(type(iphone_df['출시일'])) #<class 'pandas.core.series.Series'>