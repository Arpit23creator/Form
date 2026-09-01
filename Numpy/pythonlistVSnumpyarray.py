
a = [1, 2, 3, 4]



b = [5, 6, 7, 8]

c = a + b
print(c)

result = []

for i in range(len(a)):
    result.append(a[i] + b[i]) 

print("List: ", result)




import numpy as np 
arr_a = np.array([1, 2, 3, 4])
arr_b = np.array([5, 6, 7, 8])
arr_c = arr_a + arr_b
print("Array Addition: ", arr_c)

# numpy is fast because of vectorisation -> every operation is getting handled at once
