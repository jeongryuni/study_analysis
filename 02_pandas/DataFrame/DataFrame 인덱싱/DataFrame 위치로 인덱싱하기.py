import pandas as pd
iphone_df = pd.read_csv('../data/iphone.csv', index_col=0)
# print(iphone_df)
'''
                      출시일  디스플레이  메모리     출시 버전 Face ID
iPhone 7       2016-09-16    4.7  2GB  iOS 10.0      No
iPhone 7 Plus  2016-09-16    5.5  3GB  iOS 10.0      No
iPhone 8       2017-09-22    4.7  2GB  iOS 11.0      No
iPhone 8 Plus  2017-09-22    5.5  3GB  iOS 11.0      No
iPhone X       2017-11-03    5.8  3GB  iOS 11.1     Yes
iPhone XS      2018-09-21    5.8  4GB  iOS 12.0     Yes
iPhone XS Max  2018-09-21    6.5  4GB  iOS 12.0     Yes
'''

# print(iphone_df.iloc[2,4]) #2번 로우 4번 컬럼값 # NO
# print(iphone_df.iloc[[1,3],[1,4]]) #로우는 1,3 / 컬럼은 1,4
print(iphone_df.iloc[3:, 1:4])