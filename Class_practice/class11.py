# Tuple -> non Mutable


# number1 = [1]
# number = (1,)
# print(type(number1))
# print(type(number))

# number = (1,2,3,4,5)
# # Updating Tuple
# list1 = list(number)
# number = tuple(list1)

# # unpacking Tuple

# num1,num2,num3 = (1,2,3)
# print(num1)
# print(num2)
# print(num3)

# num1,num2,*num3 = (1,2,3,4,5)
# print(num1)
# print(num2)
# print(num3)

# num1,*num2,num3 = (1,2,3,4,5)
# print(num1)
# print(num2)
# print(num3)



#Set -> Mutable
# fruits = {"abc","xyz","cde","abc"}
# print(fruits)

# # access

# for x in fruits:
#     print(x)

# fruit = set()
# print(type(fruit))


# #addin to set
# fruit.add("abc")
# print(fruit)

# # update no update method

# set1.pop()
# # delete 
# fruit.remove("abc")
# fruit.discard("xyz")
# print(fruit)

# # clear()

# fruit.clear() # empty set

# # del
# del fruit # delete all with variable

# number = {1,0,2,3,4,True,False}
# print(number)


set1 = {1,2,3,4}
set2 = {2,4,5}
# union

# set3 = set1.union(set2)
# set3 = set1 | set2 # alternative
# print(set3)

# # union update
# set1.update(set2)
# print(set1)


# # Intersection
# set3 = set1.intersection(set2)
# print(set3)
# set3 = set1 & set2 # alternative
# print(set3)

# # intersection update
# set1.intersection_update(set2)
# print(set1)


# # Difference

# set3 = set1.difference(set2)
# print(set3)
# set3 = set1 - set2
# print(set3)

# # Difference update

# set1.difference_update(set2)
# print(set1)


# # Symmetric difference

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set3 = set1 ^ set2
# print(set3)

# # Symmetric difference update

# set1.symmetric_difference_update(set2)
# print(set1)


# # isdisjoint()
# set1 = {1,2,3,4}
# set2 = {2,4,5}
# set1.isdisjoint(set2)
# print(set1)

# # issuperset()

# set1 = {1,2,3,4}
# set2 = {2,4}

# set1.issuperset(set2)
# print(set1)


# issubset()

# set2.issubset(set1)
# print(set2)







# Question 1
# create me the bingo game using set when user enter "y" it should pick me number

number=set()
for x in range(1,100):
    number.add(str(x))

while True:
    choice = (input("Enter 'y' to pick the number else 'e' to exit: "))
    if choice.lower() == 'y':
        value = number.pop()
        print("picked number: " ,value)
    elif choice.lower()== 'e':
        print("exiting........")
        break
    if len(number) == 0 :
        print("Completed")
        break

    


# Queston 2
# generate 4-digit otp number from of number store in set

number=set()
for x in range(1000,10000):
    number.add(str(x))


while True:
    choice = (input("Enter 'y' to pick the number: "))
    if choice.lower() == 'y':
        value = number.pop()
        print("picked number: " ,value)
    
    if len(number) == 0 :
        print("Completed")
        break
