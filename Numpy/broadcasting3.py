import numpy as np

arr_a = np.array([1, 2, 3])

arr_b = np.array([
    [10],[20],[30]
])

print(arr_a.shape) # (3, )
print(arr_b.shape) # (3, 1)

'''
arr_a = 
[1, 2, 3]
[1, 2, 3]
[1, 2, 3]

arr_b = 
[10, 10, 10]
[20, 20, 20]
[30, 30, 30]
'''

print(arr_a + arr_b)

# python 

# arr_a = np.array([1,2,3]) # 1D

# arr_b = np.array([
# [10],[20],[30],
# ])


# result = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(b[i][0] + a[j])
#     result.append(row)