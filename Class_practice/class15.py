# num = 10
# def add():
#     global x 
#     x = 20
#     print (num)
# add()
# print(x)


# args

# def addition(*args): # tuple (1,2,3,4,5,6)
#     print(args)
# addition(1,2,3,4,5,6)

# kwargs

# def addition(**kwargs):
#     print(kwargs)
# addition(name = "ram",roll_no = 19)

# def addition(*args,**kwargs):
#     print(args)
#     print(kwargs)

# addition (1,2,3,4,5,6,name="ram",roll_no = 10)


# Recursive Function

# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fact(n-1)
# final_fact = fact(5)

# print("Fial_fact",final_fact)

def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

x = int(input("Enter your number for fibonacci : "))

print(fibo(x))

for i in range(x+1):
    print(fibo(i), end = " ") 
