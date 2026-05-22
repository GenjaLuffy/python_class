import csv


filepath = "D:/Python_Class/Oop_Python/output.csv"
def rollCheck():
    rolls = set()
    with open(filepath,mode = 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rolls.add(int(row['Roll_No']))
    return rolls

      


file_path = "output.csv"
with open(file_path, mode='a',newline='')as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Roll_No','Name','Age','City','Math','Science','English','Total_Marks_Obtain','Percentage','Status'])
    no = int(input("Enter how many data you want to enter : "))

    for x in range(no):
        while True:
            roll = int(input("Enter Student's Roll Number : "))
            if roll in rollCheck():
                print(f'{roll} is Already exists.')
            else:
                break
        name = input("Enter Student's Name :")
        age = input("Enter Student's Age : ")
        city = input("Enter Student's Address : ")
        math = input("Enter Student's Math Marks : ")
        science = input("Enter Student's Science Marks : ")
        english = input("Enter Student's English Marks : ")
        totalMarks = int(math)+int(science)+int(english)
        percentage = (totalMarks/300)*100
        if percentage >= 40:
            status = "Pass" 
        else:
            status = "Fail"
        csv_writer.writerow([f'{roll}',f'{name}',f'{age}',f'{city}',f'{math}',f'{science}',f'{english}',f'{totalMarks}',f'{percentage:.2f}',f'{status}'])
        print(f"{name}'s data saved!\n")
