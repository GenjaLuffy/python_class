# Read data using python

# # Method 1 and safe way
# file_path = "D:/Python_Class/Oop_Python/demofile.txt" 
# with open(file_path,'r') as file:
#     content = file.read()
#     print(content)


# # Method 2
# f = open("demofile.txt","r")
# value = f.read()
# print(value)
# f.close()

# file_path = "D:/Python_Class/Oop_Python/demofile.txt" 
# with open(file_path,'r') as file:
#     content = file.read()
#     print(content)
#     output = "Hi" + content[5:45] + "Tested." + "\nBad " + content[-6:]
#     print(output)
#     # print(type(content))


# # Method 2 for reading (readline())
# file_path = "D:/Python_Class/Oop_Python/demofile.txt" 
# with open(file_path,'r') as file:
#     row = file.readline()
#     row1 = file.readline()
#     print(row)
#     print(row1)
#     for x in file:
#         print(x , end="")


# Method 3 for reading (readlines())
# file_path = "D:/Python_Class/Oop_Python/demofile.txt" 
# with open(file_path,'r') as file:
#     row = file.readlines()
#     print(row)

# output = [x.strip("\n") for x in row]
# print(output)







# ==================================================== Day 19 ====================================================



# Write data using python


# file_path = "D:/Python_Class/Oop_Python/demofile.txt" 
# with open(file_path,'r') as file:
#     content = file.read()
#     print(content)
#     output = "Hi" + content[5:45] + "Tested." + "\nBad " + content[-6:]
#     print(output)
#     # print(type(content)) 
# with open("demofile1.txt",'w') as file:
#     content = file.write(f"{output}\n")
#     print(content)




# import csv
# filepath = "D:/Python_Class/Oop_Python/data.csv"
# # Reading csv file using csv.reader
# with open(filepath,mode = 'r') as file:
#     csv_reader = csv.reader(file)
#     # header = next(csv_reader)
#     # print(header)
#     for row in csv_reader:
#         print(row[1])



import csv

file_path = "output.csv"
with open(file_path, mode='w',newline='')as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Name','Age','City'])
    no = int(input("Enter how many data you want to enter : "))

    for x in range(no):
        name = input("Enter Name :")
        age = input("Enter Age : ")
        city = input("Enter City : ")
        csv_writer.writerow([f'{name}',f'{age}',f'{city}'])

    