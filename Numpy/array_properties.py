import numpy as np

arr = np.array([1, 2, 3, 4]) # 1d Array

# print(arr.shape) # (4, )

arr2 = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90],
  [75, 85, 95]
])
# print(arr2.shape) #(4, 3)

# print(arr.ndim)
# print(arr2.ndim)

# print(arr.size)
# print(arr2.size)

# print(arr.dtype)
# print(arr2.dtype)

#Indexing and slicing
arr2 = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90],
  [75, 85, 95]
])

# print(arr2[0, 1])

# print(arr2[0:3, 2])
# print(arr2[0:3, -1])  # -1 refers to the last item

# print(arr2[1:4, :])

arr2 = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90],
  [75, 85, 95]
])

print(np.sum(arr2, axis=0)) # column wise
print(np.sum(arr2, axis=1))  # row wise

# np.mean(arr)
# np.max(arr)
# np.min(arr)

