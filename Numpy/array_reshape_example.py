import numpy as np

arr2 = np.array([
  [10, 20, 30],
  [40, 50, 60],
  [70, 80, 90],
  [75, 85, 95]
])

print(arr2.shape)

# can only reshape data such that data does not change

print(arr2.reshape(2, 6))

print(arr2.reshape(3, 4))

#flattening the array
print(arr2.reshape(12))