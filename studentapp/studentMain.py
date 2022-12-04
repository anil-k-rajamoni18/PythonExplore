from studentUtil import *


while True:
    print("\n 1.studentFunctions()\n 2.studentJobs()\n 3.studentAssignments()\n 4.addstudentfunction\n 5.addstudent()\n -1.exit")
    studentChoice = int(input("Enter your choice:"))
    print(studentChoice)
    

    if studentChoice == 1:
        studentId = input("enter student id:")
        res = getStudentFunctions(studentId)
        print(res)

    elif studentChoice == 2:
        studentId = input("enter student id:")
        res = getStudentJobs(studentId)
        print(res)

    elif studentChoice == 3:
        studentId = input("enter student id:")
        res = getStudentAssignments(studentId)
        print(res)
    
    elif studentChoice == 4:
        studentId = input("enter student id:")
        funcName = input("enter student function name:")
        res = addStudentFunction(funcName, studentId)
        print(res)

    elif studentChoice == 5:
        name = input("enter student name:")
        degree = input("enter student degree:")
        res =addStudent(name=name,degree=degree)
        print(res)
    

    elif studentChoice == -1:
        break

    else:
        print("Invalid Input")

