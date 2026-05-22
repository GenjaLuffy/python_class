# # Sort
# number = [4,6,3,6,3,7]
# number.sort()
# print(number)

# number.sort(reverse=True)
# print(number)


# fruits = ["pine","orange","apple","banana","apples","Zoo"] # sort in this order A-Z and a-z
# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)


# # Sorted 
# number = [4,6,3,6,3,7]
# new_number = sorted(number)
# print(new_number)

# new_number = sorted(number,reverse=True)
# print(new_number)




# Copy

# number = [1,2,3,4,5]
# new_number = number.copy()  # method 1
# # new_number = list(number)  # method 2
# # new_number = number[:]  # method 3

# print("number :" , number)
# print("new_number :" , new_number)

# number.append(100)
# print("-------------------After-------------------")
# print("number :" , number)
# print("new_number :" , new_number)


# Update

# num1 = [1,2,3,4,5]
# num2 = [6,7,8,9]
# num3 = num1 + num2 # Optional

# num1.extend(num2)
# print(num1)



# # List Comprehention

# # normal approach
# fruits = ["apple", "banana", "cherry"]
# new_fruit=[]
# for x in fruits:
#     if "a" in x:
#         new_fruit.append(x)
# print("new_fruits", new_fruit)


# # List Comprehention approach
fruits = ["apple", "banana", "cherry"]
new_fruit=[x for x in fruits if "a" in x]
print("new_fruits", new_fruit)

# # normal approach
# number = [1,2,3,4,5,6,7,8]
# new_number=[]
# for x in number:
#     if x % 2 == 0:
#         new_number.append("e")
#     else:
#         new_number.append("o")
# print(new_number)

# # List Comprehention approach
# number = [1,2,3,4,5,6,7,8]
# new_number=["e" if x % 2 == 0 else "o" for x in number]
# print(new_number)


# # normal approach
# number = [1,2,3,4,5,6,7,8]
# new_number=[]
# for x in number:
#     new_number.append(x ** 2)
# print(new_number)

# # List Comprehention approach
# number = [1,2,3,4,5,6,7,8]
# new_number = [x ** 2 for x in number]
# print(new_number)

# value = f"Hello! {name1}. Hi {name2}"



# # Question 1
# number = [1,2,3,4,5,6,7,8]
# # new_number = ["2-Even","4-Even","6-Even","8-Even"]  # Output
# new_number =[f"{x}-Even" for x in number if x % 2 == 0 ]
# print(new_number)


# # Question 2
# fruits = ["apple","banana","ggg","hhh","ffff"]
# # new_fruits = ["vowel","vowel","vowel","non-vowel","non-vowel","non-vowel"]
# vowel = "aeiouAEIOU"
# new_fruit=["Vowel" if any(char in vowel for char in x) else "Non-Vowel" for x in fruits]
# print(new_fruit)


# # Question 3 
# numbers = [1,2,3,4,5]
# # new_numbers = [4,2,6,4,8]
# new_numbers = [x + 3 if x % 2 != 0 else x for x in numbers]
# print(new_numbers)

# # Question 4
# fruit = ["APPLE","cherry","BANANA","orange","PINE"]
# # new_fruit = ["apple","CHERRY","banana","ORANGE","pine"]
# new_fruit = [x.lower() if x.isupper() else x.upper() for x in fruit]
# print(new_fruit)