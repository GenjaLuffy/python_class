# Functions

# Method_1 : Parameterless non return type function


# def addiction():
#     x = int(input("Enter num_1 : "))
#     y = int(input("Enter num_2 : "))
#     print(f"The Addition of {x} and  {y} is", x+y)
    
# addiction()


# Method_2 : Paramaters non return type function

# def addition(num1,num2):
#     result = num1 + num2
#     print("result : ", result)

# x = 50
# y = 90
# addition(20,30)
# addition(x,y)


# Method_3 : Paramaterless return type function

# def addiction():
#     x = int(input("Enter num_1 : "))
#     y = int(input("Enter num_2 : "))
#     result = x+y
#     return result

    
# final_result = addiction()
# print(final_result)


# Method_4 : Paramater with return type fuction

# def addition(x,y):
#     result = x + y
#     return result


# x = int(input("Enter num_1 : "))
# y = int(input("Enter num_2 : "))
# final_result = addition(x,y)
# print(final_result)



def add():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    print(f"The Sum of {x} and {y} = ",x+y)

def sub(num1, num2):
    result= num1-num2
    print(result)

def mul():
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : "))
    result = x*y
    return result

def division(value1,value2):
    result = value1/value2
    return result



while True:
    choice = int(input("Press '1' to addition : \nPress '2' to subtractionn : \nPress '3' for multiplication : \nPress'4' for division : \nPress '5' for exit"))
    if choice == 1:
        add()
    elif choice == 2:
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        sub(num1,num2)
    elif choice == 3:
        final_result = mul()
        print("Result = ",final_result)
    elif choice == 4:
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        final_result = division(num1,num2)
        print("Result = ",final_result)
    elif choice == 5:
        print("Have a Great Day")
        break
    else:
        print("Invalid Choice")
        break
    break




# def calculator(x,y):
#     add = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     return add,sub,mul,div

# x = int(input("Enter num1 : "))
# y = int(input("Enter num2 : "))

# final_result = calculator(x,y)
# add,sub,mul,div = final_result
# print(add)
# print(sub)
# print(mul)
# print(div)

# def calculator(x):
#     maximum = max(x)
#     minimum = min(x)
#     total = sum(x)
#     return maximum,minimum,total

# numbers = [1,2,3,4,5]

# final_result = calculator(numbers)
# print(final_result)