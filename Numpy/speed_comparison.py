import time

import numpy as np

size = 1000000

list_a = list(range(size)) # []
list_b = list(range(size)) 
result = list_b + list_a
start = time.time()

for i in range(len(list_a)):
    result.append(list_a[i] + list_b[i]) 


end = time.time()

print("List addition", end - start)

arr_a = np.array(list_a)
arr_b = np.array(list_b)

start = time.time()
result = arr_a + arr_b
end = time.time()

print("Array calulation: ", end-start)
