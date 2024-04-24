#%%
import numpy
#%%
# 파이썬 리스트를 통해 생성
# numpy 모듈의 array 메소드에 파라미터로 파이썬 리스트를 넘겨주면 numpy array가 리턴됩니다.
array1 = numpy.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
print(array1) # [ 2  3  5  7 11 13 17 19 23 29 31]
#%%
# array1의 타입
print(type(array1)) # <class 'numpy.ndarray'>
#%%
# array1의 요소
print(array1.shape) # (11,) 11개의 요소가 있다.
#%%
# 2차원 array
array2 = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(array2)
print(array2.shape) # (3, 4) 행:3 열:4
#%%
# 요소의 개수를 알려줌
print(array1.size) # 11
print(array2.size) # 12
#%%
# 균일한 값으로 생성
array1 = numpy.full(6, 7)

print(array1) # [7 7 7 7 7 7]
#%%
# 모든 값이 0인 numpy array 생성
array1 = numpy.full(6, 0)
array2 = numpy.zeros(6, dtype=int)

print(array1)
print()
print(array2)
#%%
# 모든 값이 1인 numpy array 생성
array1 = numpy.full(6, 1)
array2 = numpy.ones(6, dtype=int)

print(array1)
print()
print(array2)
#%%
# 랜덤한 값들로 생성
array1 = numpy.random.random(6)
array2 = numpy.random.random(6)

print(array1)
print()
print(array2)
#%%
# 연속된 값들이 담긴 numpy array 생성
# arange(m)을 하면 0부터 m-1까지의 값들이 담긴 numpy array가 리턴됩니다.

# 파라미터 1개
array1 = numpy.arange(6)
print(array1) # [0 1 2 3 4 5]


# 파라미터 2개
array1 = numpy.arange(2, 7)
print(array1) # [2 3 4 5 6]


# 파라미터 3개
# arange(n, m, s)를 하면 n부터 m-1까지의 값들 중 간격이 s인 값들이 담긴 numpy array가 리턴됩니다.
array1 = numpy.arange(3, 17, 3)
print(array1) #  [3  6  9 12 15]


#%%
