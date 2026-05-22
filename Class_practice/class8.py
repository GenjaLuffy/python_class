# list

# numbers = [1,2,3,4,5]

# fruits = ['apple', 'banana', 'cherry']

# mixed_list = [10, 'hello', True , 3.14]

numbers = [1,2,3,4,5]

# for x in numbers:
#     print(x)

# for x in range(len(numbers)):
#     print(x)

# print(numbers[1:4])


# Modificattion

# # Update
# numbers[2] = 100
# print(numbers)

# # add to thhe end of list

numbers.append(200)

# #insert
# numbers.insert(1,500)

# # Delete
# numbers.remove(500)
# print(numbers)

# numbers.pop()
# print(numbers)

# numbers.clear()
# print(numbers)

# del numbers[2]
# print(numbers)

# del numbers # delete veriable


# Question 1
fruits = ["apple","banana", "cherry","pine","orAnge"]
#scan above list and remove all the element that have "a"in it

# Question 2 
numbers = [1,2,3,4,5,6,7,8]
#scan above list and update all the even value in above list with 'EVEN'

# Question 3
number = [1,1,1,2,3,4,5,3]
# scan above list and create the new list with only unique value

# Question 4
fruit = ["apple", "banana", "cherry", "gggg", "fff", "hhh"]
#scan above list and remove non vowel word from list

# fruits = [fruit for fruit in fruits if "a" not in fruit.lower()]
value = list(fruits)
for x in fruits:
    if "a" in x.lower():
        value.remove(x)
print(value)



# numbers = ["EVEN" if num % 2 == 0 else num for num in numbers]
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = "EVEN"
print(numbers)


# new_numbers = []
# for num in number:
#     if num not in new_numbers:
#         new_numbers.append(num)
# print(new_numbers) 


new_number = list(number)
for x in number:
    if number.count(x) > 1:
        for y in range(number.count(x)-1):
            new_number.remove(x)
print(new_number)


# vowels = "aeiouAEIOU"
# fruit = [word for word in fruit if any(char in vowels for char in word)]

# print(fruit)


new_fruit = list(fruit)
vowels = "aeiouAEIOU"

for value in fruit:
    flag = False
    for x in value:
        if x in vowels:
            flag = True
            break
    if not flag:
        new_fruit.remove(value)
print(new_fruit)

