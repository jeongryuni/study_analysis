import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)
# print(iphone_df)
# print(iphone_df.loc[[True, False, True, True, False, True, False]]) #인덱스가 트루인곳만 출력
# print(iphone_df.loc[[True, False, False, True]]) # 현재 개수에 맞는 리스트 요소를 전부 적어야함
# print(iphone_df.loc[:,[True, False, True, True, False, True, False]])

# print(iphone_df['디스플레이']>5) # 디스플레이가 5보다 크면 True로 나옴

# print(iphone_df.loc[iphone_df['디스플레이']>5]) # 디스플레이가 5보다 큰 것들만 출력
# print(iphone_df.loc[iphone_df['Face ID'] == 'Yes']) # 페이스ID가 Yes인 애들만 출력

# 디스플레이가 5인치보다 크고 FaceID가 Yes인 것들
# condition = (iphone_df['디스플레이']>5) & (iphone_df['Face ID'] == 'Yes')
# print(iphone_df[condition])

# 디스플레이가 5인치보다 크고 FaceID가 Yes인 것을 하나만 충족해도 된다면
condition = (iphone_df['디스플레이']>5) | (iphone_df['Face ID'] == 'Yes')
print(iphone_df[condition])
#
