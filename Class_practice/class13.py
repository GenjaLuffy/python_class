# student = {
#     "name" : "ram",
#     "roll" : 12,
#     "address" : "Kathmandu",
#     "contact" :{
#         "email" : "ram.123@mail.com",
#         "phone_no" : [1234567890, 9804512235],
#     },
#     "subject" : {
#         "math" : 20,
#         "science" : 50,
#         "computer" : 60
#     },
#     "age" : 20
# }

# print(student["contact"]["phone_no"][0])

# for k,v in student.items():
#     if k == "contact" or k == "subject":
#         for key,value in v.items():
#             print(f"{key}:{value}")

# value = student["subject"]
# value1=value.values()
# value["Total_marks"] = sum(value1)
# print(student["subject"]["Total_marks"])
# total_marks = value["math"] + value["science"] + value["computer"]
# student["subject"]["total_marks"] = total_marks
# print(student["subject"]["total_marks"])



# student = {}
# contact = {}
# subject = {}
 

# student["name"]=(input("Enter Your Name :"))
# student["roll"]=int(input("Enter Your Roll_Number : "))
# student["address"] =(input("Enter Your Address :"))
# student["age"] =int(input("Enter Your Age : "))

# contact["email"] = input("Enter your Email address : ")


# phone_no = []
# phone = int(input("How many number do you like to keep : "))
# while phone !=0:
#     number = int(input("Enter Your Number"))
#     if len(str(number)) and (str(number)).isdigit():
#         phone_no.append(number)
#         phone -=1
#     else:
#         print("Invalid Number!!")
# student["contact"] = contact


# subject ["math"] = int(input("Enter your Math Marks : "))
# subject["science"] = int(input("Enter your Science Marks : "))
# subject["computer"] = int(input("Enter your Computer Marks : "))
# student["subject"] = subject
# print("------------------- Result -------------------")
# print(student)

# phone_no = []
# phone = int(input("How many number do you like to keep : "))
# while phone !=0:
#     number = int(input("Enter Your Number"))
#     if len(str(number)) and (str(number)).isdigit():
#         phone_no.append(number)
#         phone -=1
#     else:
#         print("Invalid Number!!")

students = {}

while True :
    student = {}
    contact = {}
    subject = {}
    phone_no = []

    student["name"]=(input("Enter Your Name :"))
    student["roll"]=int(input("Enter Your Roll_Number : "))
    student["address"] =(input("Enter Your Address :"))
    student["age"] =int(input("Enter Your Age : "))

    no_phone = int(input("How many number do you like to keep : "))
    while no_phone !=0:
        number = int(input("Enter Your Number : "))
        if len(str(number)) and (str(number)).isdigit():
            phone_no.append(number)
            no_phone -=1
        else:
            print("Invalid Number!!")
    contact["phone_number"] = phone_no
    student["contact"] = contact


    subject ["math"] = int(input("Enter your Math Marks : "))
    subject["science"] = int(input("Enter your Science Marks : "))
    subject["computer"] = int(input("Enter your Computer Marks : "))
    
    student["subject"] = subject

    students[f"roll_no:{student['roll']}"] = student

    choice = input("Do you want to add more Student.\nPress 'yes' or 'y' for continue 'no' or 'n' for exit : ").lower()
    
    if choice == 'no' and 'n':
        print("Exiting.....")
        break

    elif choice not in ('y' and 'yes'):
        print("Invalid input. \n Exiting......")
        break

print(students)