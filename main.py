student_details = {}


def remove():
    while True:
        print("Removing a Student Record:")
        student = input("Enter the student name you want to remove (enter exit to return):")
        rem = student.capitalize()
        if rem in student_details.keys():
            student = student.capitalize()
            student_details.pop(student)
            print("Student Record have been removed")
            print(student_details)
        elif student == "exit":
            menu()
            break


def add():
    # check = True
    while True:
        print("\nAdding New Student:")
        name = input("Enter your name (enter exit to return): ")
        course = input("Enter your course (enter exit to return):")
        gpa = input("Enter your GPA (enter exit to return):")
        if name.lower() == "exit" or course.lower() == "exit" or gpa.lower() == "exit":
            # check = False
            break
        else:
            name = name.capitalize()
            gpa = float(gpa)
            student_details[name] = course, gpa



def menu():
    while True:
        print("Welcome to the student dictionary")
        print("1. Add student")
        print("2. Remove student")
        print("3. View Dictionary")
        print("0. Exit program")
        option = int(input("Enter your choice:"))
        if option == 1:
            add()
        elif option == 2:
            remove()
        elif option == 3:
            print(student_details)
        elif option == 0:
            print("Goodbye~")
            break
        else:
            print("Please select a valid option")


menu()
