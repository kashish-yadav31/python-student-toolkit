def process_student():
    print("Welcome to Student Toolkit")
    name = input("Enter student name:")
    roll_no = input("Enter roll number:")

    print("\nStudent Deatails")
    print("Name:", name)
    print("Roll no:", roll_no)

    print("\nEnter Marks")

    maths = int(input("Enter Maths marks:"))
    science = int(input("Enter Science marks:"))
    english = int(input("Enter English marks:"))

    total = maths + science + english
    percentage = total / 3

    print("\nResult")
    print("Total Marks:", total)
    print("Percentage:", percentage)

    if percentage >= 40:
        print("Status: Pass")
    else:
        print("Status: Fail")


num = int(input("How many students to process? "))

for i in range(num):
    print("\nProcessing student", i + 1)
    process_student()
