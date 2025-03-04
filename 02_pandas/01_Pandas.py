import pandas as pd
import numpy as np

two_dimensional_list = [['dongwook',50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91,], ['jeongryun', 82, 83]]
my_df = pd.DataFrame(two_dimensional_list, columns=['name', 'eng_score', 'math_score'], index=['a','b','c','d'])

print(my_df)
'''
        name  eng_score  math_score
a   dongwook         50          86
b     sineui         89          31
c    ikjoong         68          91
d  jeongryun         82          83
'''

print(type(my_df)) #<class '02_pandas.core.frame.DataFrame'>
print(my_df.columns) #Index(['name', 'eng_score', 'math_score'], dtype='object')
print(my_df.index) #Index(['a', 'b', 'c', 'd'], dtype='object')
print(my_df.dtypes)

'''
같은 칼럼내에서는 동일한 타입이어야한다.

name          object
eng_score      int64
math_score     int64
dtype: object
'''

# DataFrame을 만드는 다양한 방법
#
# 2차원 리스트나 2차원 01_numpy array로 DataFrame을 만들 수 있습니다.
# 심지어 02_pandas Series를 담고 있는 리스트로도 DataFrame을 만들 수 있습니다.

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]),
    pd.Series(['sineui', 89, 31]),
    pd.Series(['ikjoong', 68, 91]),
    pd.Series(['yoonsoo', 88, 75])
]
# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)
'''
          0   1   2
0  dongwook  50  86
1    sineui  89  31
2   ikjoong  68  91
3   yoonsoo  88  75

'''


# 파이썬 딕셔너리(dictionary)으로도 DataFrame을 만들 수 있습니다.
# 사전의 key로는 column 이름을 쓰고,
# 그 column에 해당하는 리스트, 01_numpy array, 혹은 02_pandas Series를 딕셔너리의 value로 넣어주면 됩니다.

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names,
    'english_score': english_scores,
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names),
    'english_score': np.array(english_scores),
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names),
    'english_score': pd.Series(english_scores),
    'math_score': pd.Series(math_scores)
}

# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)
print(df1)

#리스트가 담긴 사전이 아니라, 딕셔너리이 담긴 리스트로도 DataFrame을 만들 수 있습니다.

my_list = [
    {'name': 'dongwook', 'english_score': 50, 'math_score': 86},
    {'name': 'sineui', 'english_score': 89, 'math_score': 31},
    {'name': 'ikjoong', 'english_score': 68, 'math_score': 91},
    {'name': 'yoonsoo', 'english_score': 88, 'math_score': 75}
]

df = pd.DataFrame(my_list)
print(df)