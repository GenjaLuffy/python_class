# Error Handleing


# Method 1 usinf try with multiple except block
# try:
#     num1 = int(input("Enter Your first Number : "))
#     num2 = int(input("Enter Your Second Number : "))
#     result = num1/num2
#     print("Result",result)
# except ZeroDivisionError as e:
#     print(e)  
#     print("You can't divide a number by Zero")

# except ValueError as e:
#     print(e)
#     print("You Must Enter Valid number")


# def divide():
#     try:
#         num1 = int(input("Enter Your first Number : "))
#         num2 = int(input("Enter Your Second Number : "))
#         result = num1/num2
#         print("Result",result)
#     except ZeroDivisionError as e:
#         print(e)  
#         print("You can't divide a number by Zero")
#         divide()


# divide()


# Method 2  using try with  single except block 

# try:
#     num1 = int(input("Enter Your first Number : "))
#     num2 = int(input("Enter Your Second Number : "))
#     result = num1/num2
#     print("Result",result)
# except Exception as e:
#     print(e)  
#     print("You have some issue on input")



# Method 3 Custom Exeption with single exception block

# age = int(input("Enter Your Age : "))
# try:
#     if age < 0 or age > 120:
#         raise Exception("Age must be between 0 to 120")
# except Exception as e:
#     print(e)


# Method 4 Custom Exeption with multiple exception block


# class ZeroError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)

# class HigestError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(message)

# try:
#     age = int(input("Enter Your Age : "))
#     if age < 0 :
#         raise ZeroError("Age must be greater than 0")
#     elif age > 120 :
#         raise ZeroError("Age must be less than 120")
        
# except ZeroError as e :
#     print(e)

# except HigestError as e :
#     print(e)


# Trace Back the error to debug the program

# import traceback
# try:
#     num1 = int(input("Enter Your first Number : "))
#     num2 = int(input("Enter Your Second Number : "))
#     result = num1/num2
#     print("Result",result)
# except Exception as e:
#     traceback.print_exc()
#     print(e)  
#     print("You have some issue on input")




value  = input("Enter your numebr : ")
try:
    if value.isdigit():
        value = int(value)
        print("Your Entered numebr is ", value)
    elif "." in value :
        value = float(value)
        print("Your Entered Numebr is :",value)

except Exception as e:
    print(e)
    print(("You have entered invalid input"))
