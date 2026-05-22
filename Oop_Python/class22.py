# # Custom Import from My_Module_class22.py 

# # Method 1
# import My_Module_Class22
# My_Module_Class22.greeting('Ram')


# # Method 2
# import My_Module_Class22 as m
# m.greeting('Hari')


# # Method 3 
# from My_Module_Class22 import greeting,add
# greeting("Shyam")
# add(2,5)


# # Method 4
# from My_Module_Class22 import greeting as g,add as a
# greeting("Shyam")
# g("Sita")
# add(2,5)
# a(8,9)



# import My_Module_Class22 as m
# choice = 0
# while True:
#     choice = int(input ("Enter 1 for Addintion\nEnter 2 for Subtraction\nEnter 3 for Multiplication\nEnter 4 for Division\nEnter 5 for Exiting \n"))
#     if choice == 1:
#         num1 = int(input("Enter num1 :"))
#         num2 = int(input("Enter num2 :"))
#         m.add(num1,num2)
#         break
#     elif choice == 2:
#         num1 = int(input("Enter num1 :"))
#         num2 = int(input("Enter num2 :"))
#         m.sub(num1,num2)
#         break
#     elif choice == 3:
#         num1 = int(input("Enter num1 :"))
#         num2 = int(input("Enter num2 :"))
#         m.mul(num1,num2)
#         break
#     elif choice == 4:
#         num1 = int(input("Enter num1 :"))
#         num2 = int(input("Enter num2 :"))
#         m.div(num1,num2)
#         break
#     elif choice == 5:
#         print("Exiting.....")
#         break
#     else:
#         print("Invalid Number....")
#         break



# Without Paramater function and without paramater deccorator

# def decorator1(x):
#     def wrapper():
#         print("Something before funtion runs.")
#         x()
#         print('hi')
#         print('bye')
#     return wrapper
    
# @decorator1
# def say_hello():
#     print("Hello")

# say_hello()


# With Paramater function and without paramater decorator

# def decorator1(fun):
#     def wrapper(*args,**kwargs):
#         print('Something before function runs.')
#         fun(*args,**kwargs)
#         print('Something after function runs.')
#     return wrapper

# @ decorator1
# def say_hello(x,y):
#     print("Hello",x,y)
    
# say_hello('abc','xyz')


# With Paramater function and with paramater decorator


# def great_decorator(greetings):
#     def decorator1(fun):
#         def wrapper(*args,**kwargs):
#             print(f'{greetings} before function runs')
#             fun(*args,**kwargs)
#             print('Something after function runs.')
#         return wrapper
#     return decorator1

# @ great_decorator("Hello")
# def say_hello(a,b):
#     print("a and b",a,b)
    
# say_hello(1,2)


import time

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)
        end_time = time.time()
        print(f'Execution time of {start_time-end_time:.4f} second')
    return wrapper
@execution_time
def example_function():
    