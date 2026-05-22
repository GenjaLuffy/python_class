# #.replace only replace while printing only not change in stored data
s = "Hello , World"
print(s)
print(s.replace("World", "Python"))

# #.lower only replace while printing only not change in stored data
# s = "Hello , World"
# print(s)
# print(s.lower())

# #.upper only replace while printing only not change in stored data
# s = "Hello , World"
# print(s)
# print(s.upper())

# #.title only replace while printing only not change in stored data
# s = "hello , world"
# print(s)
# print(s.title())


#strip remove the unwanted space while printing or while running the program

# s = "         hello , world         "
# print(s.lstrip())

# s = "         hello , world         "
# print(s.rstrip())

# s = "         hello , world         "
# print(s.strip())





# s = "hello, world"
# value = s.split()
# print(value)


# list = ['Hello', 'Worlld']

# value = ' '.join(list)
# print(value)




# s = "12345"
# print(s.isdigit())


# s= "HELLO"
# print(s.isupper())

# s= "HELLO"
# print(s.islower())



# s = "Hello, {}"
# print(s.format("Python"))

# name = input("Enterr Your Name : ")
# value = "HEllo! {}".format(name)

# name1 = input("Enterr Your Name1 : ")
# name2 = input("Enterr Your Name2 : ")
# value = f"Hello! {name1}. Hi {name2}"
# # value = "Hello! {}, Hi {}".format(name1,name2)
# print(value)

# Question 1
# Take input form user as string check the word have vowel character in it and count them

# Question 2
#convert the input string format withoput using replace
# input_string = "#@!#@!##@!%#!!@#!@#!@#!@#Hello#@@World!@#!@#!@#"
# output_string = "Hello World"



# word = input("Enter any Word : ")
# count = 0
# for i in word.lower():
#     if i in "aeiou":
#         count+=1

# if count == 0:
#     print("There is no vowel letter")
# else:
#     print(f"There is vowel letter.Count {count}")

# input_string = "#@!#@!##@!%#!!@#!@#!@#!@#hello#@@#!@#!@#!@#!@#world!@#!@#!@#"
# output_string = "Hello World"
# value1 = input_string.strip("#@!%").split("#@@")
# print(value1)