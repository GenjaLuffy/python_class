
student = {
    "name" : "ram",
    "roll" : 12,
    "address" : "Kathmandu",
    "phone no." : "9845542215",
    "marks" : [70,50,60,40,40],
    "age" : 20
}

#access
# print(student(["roll"]))

print(student.get("address","Kathmandu"))

# loop

# for x in student:
#     print(f"{x} : {student[x]}")
    
for x in student.keys():
    print(x)
        
# for values in student.values():
#     print(values)

# for value in student.items():
#     print(value)

# for key,value in student.items():
#     print(key,":",value)


# # Add / Upadate

# student["total_marks"] = 500
# student["age"] = 25

# for key,value in student.items():
#     print(key,":",value)

# # Delete

# student.pop("age")
# student.clear()
# del student
# for key,value in student.items():
#     print(key,":",value)


# student = {
#     "name" : "ram",
#     "roll" : 12,
#     "address" : "Kathmandu",
#     "phone no." : "9845542215",
#     "marks" : [70,50,60,40,40],
#     "age" : 20
# }
# student["total_marks"] = sum(student["marks"])

# for key,value in student.items():
#     print(key,":",value)


# student = {}
# choice = 0
# choice1 = 0
# phone = []
# student["name"]=(input("Enter Your Name :"))
# student["roll"]=int(input("Enter Your Roll_Number : "))
# student["address"] =(input("Enter Your Address :"))
# student["age"] =int(input("Enter Your Age : "))
# choice =int(input("How many number do you like to keep : "))
# while choice:
#     phones = input("Enter your Phone Number: ").strip()
#     if not phones.isdigit() or len(phones) != 10 or phone == 0:
#         print("Invalid number: Phone number must be exactly 10 digits.")
#     else:
#         phone.append(int(phones))
#         # print(f"Phone number {phones} added successfully!")   
#         another = input("Add another phone number? (y/n): ").strip().lower()
#         if another != "y":
#             break  # Stop loop if user doesn't want to add more
#     student["phone_no"] = phone

#     break  # Only break when valid input is received

# for key,value in student.items():
#     print(key,":",value)