# Matplot in python

# import matplotlib.pyplot as plt

# x = [1,2,3,4,5]
# y = [2,3,5,7,11]
# x1 = [6,7,8,9,10]
# y1 = [2,3,5,7,11]

# plt.plot(x,y , marker = 'o',linestyle = '--',color = 'b',label = 'Prime Numbers')
# plt.plot(x1,y1 , marker = 'o',linestyle = '-',color = 'r',label = 'Numbers')
# plt.xlabel('X-Axis')
# plt.ylabel('Y-Axis')
# plt.title('Prime Numbers Plots')
# plt.legend()
# plt.show()




# # Lamda Function

# square = lambda x : x**2
# print(square(5))

# add = lambda a,b : a+b
# print(add(5,5))



# # Map

# numbers = [1,2,3,4,5]
# # squared = list(map(lambda x : x **2, numbers))
# # print(squared)

# def calc(x):
#     result1 = x+1
#     result2 = x ** 2 
#     return result2

# value = map(calc,numbers)
# print(list(value))





# # Filter in python 
# numbers = [1,2,3,4,5,6,7,8,9,10]
# # even_numbers = list(filter(lambda x : x%2 == 0, numbers))
# # print(even_numbers)


# def even(x):
#     result = x % 2 == 0
#     return result

# values = filter(even,numbers)
# print(list(values))



# from functools import reduce

# numbers = [1,2,3,4,5]
# sum = reduce(lambda x,y : x+y,numbers)
# print(sum)

# numbers = [3,8,1,6,2]
# max = reduce(lambda x, y : x if x > y else y,numbers)
# print(max)

# numbers = [1,2,3,4,5]
# product = reduce(lambda x, y : x * y , numbers ,1)
# print(product)


# import os

# current_dir = os.getcwd()
# print(current_dir)

# files = os.listdir(current_dir)
# print(f'{current_dir}'+f'{+files}')


import random

random_number = random.randint(1,10)
print(random_number)

# Suffel list
numbers = [1,2,3,4,5]
random.shuffle(numbers)
print(numbers)