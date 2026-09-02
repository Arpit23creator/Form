import numpy as np

# print(np.random.rand(10)) rand is a function that numpy uses to create arrays with uniformly distributed numbers between 0 and 1

# print(np.random.rand(3, 4))
# gaussian distribution -> mean = 0 and standard deviation = 1
# print(np.random.randn(10))

# print(np.random.randint(0, 10))

# print(np.random.randint(0, 10, 6))

# print(np.random.randint(0, 10, size=(3, 4))) #2D

#np.random.seed(42)

# print(np.random.rand(2, 3))

#Shuffle

arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
print(arr)

#Example without shuffle function
# 0 -> Not spam and 1 -> Spam
data = np.array([0, 0, 0, 0, 1, 1, 1, 1])

#Split (first 75% train, rest test)
train = data[:6]
test = data[6:]

print("Train:", train)
print("Test:", test)

# Example with shuffle function

