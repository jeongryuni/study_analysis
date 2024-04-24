#%%
import numpy as np
#%%
array1 = np.array([2, 3, 5, 7, 11, 13, 17 ,19 , 23, 29, 31])
#%%
array1 > 4
#%%
array1 % 2 == 0
#%%
booleans = np.array([True, True, False, True, False, True])
#%%
np.where(booleans)
#%%
array1 > 4
#%%
np.where(array1 > 4) # 4보다 큰 값이 있는 인덱스만 가져옴
#%%
# filter를 이용해 인덱싱을 할 수있다.
filter = np.where(array1 > 4)
filter
#%%
array1[filter] # 4보다 큰 값들만 인덱싱
#%%
