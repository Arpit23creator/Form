# def check_leap_year(year):
    
#     if(year % 100 == 0):
#         if(year % 400 == 0):
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not leap year.")
#     else:
#         if(year % 4 == 0):
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")

# year = 2024
# check_leap_year(year)

# my_list = [1, 2, 2, 3 , 4, 4, 5, 5]

# my_set = set(my_list)

# print(my_set)

# my_list = list(my_set)
# print(my_list)

# fruits =["Apple", "Mango", "Banana", "Cherry"]

# print(fruits)   

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# n = 5
# print(factorial(n))


# '''
# Deepak is a big lodu , very very big lodu.

# '''

# str = "Deepak Lodu"
# # print(str[::-1])

# str1 = "".join(reversed(str))
# print(str1)

# string = "Hello world       "
# print(string.strip())

# print(string.split())

# list = [1, 2, 3, 4, 5, 6, 7]
# list.extend([8, 9, 10])
# print(list)

# print(list.count(1))

# d = dict({'white':'1', 'green':'2', 'yellow':'3', 'blue':'4'})
# print(d)
# print(len(d))
# print(d.sorted())

def fibonacci(n):
    if n<=1: return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 5
for i in range(0, n+1):
    print(fibonacci(i))
