import numpy as np

arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

arr_1d = np.array([10, 20, 30])


''' 
broadcasting -> numpy will expand smaller dim array into higher
dimension (does not convert in real just acts like it)
-> saves memory
-> faster computation 
actual calculation done by numpy is done in C.
'''
'''
[10, 20, 30],
[10, 20, 30],
[10, 20, 30]
'''
print(arr_1d.shape)
print(arr_2d.shape)

print(arr_2d + arr_1d)