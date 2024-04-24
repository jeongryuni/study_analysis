import pandas as pd

samsong_df = pd.read_csv('../data/samsong.csv')
hyundee_df = pd.read_csv('../data/hyundee.csv')

#print(samsong_df)
samsong_df = (samsong_df.loc[:,['요일','문화생활비']])
hyundee_df = (hyundee_df.loc[:,'문화생활비'])

card_df = pd.concat([samsong_df, hyundee_df], axis=1) # axis=1 수평 연결 / 0은 아래로 연결

card_df.columns = ['day', 'samsong', 'hyundee']
print(card_df)

'''
   day  samsong  hyundee
0  MON     4308     5339
1  TUE     7644     3524
2  WED     5674     5364
3  THU     8621     9942
4  FRI    23052    33511
5  SAT    15330    19397
6  SUN    19030    19925

'''