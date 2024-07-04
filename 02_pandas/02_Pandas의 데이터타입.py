import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]

my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'english_score', 'math_score'], index=['a', 'b', 'c', 'd'])

print(my_df.dtypes)

'''
한 column 내에서는 모든 값이 동일한 데이터 타입입니다.

name             object
english_score     int64
math_score        int64
dtype: object
'''

'''
pandas의 dtype들
pandas에 담을 수 있는 dtype(데이터 타입) 몇 가지를 살펴봅시다.

int64	정수
float64	소수
object	텍스트
bool	불린(참과 거짓)
datetime64	날짜와 시간
category	카테고리

'''