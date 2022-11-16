def student_gpa(grades_list):
    avarage=sum(grades_list)/len(grades_list)
    if avarage<=100 and avarage>=93:
        print(f"Student Avarage is :{avarage} and GPA is 4.0")
    elif avarage<=92 and avarage>=90:
        print(f"Student Avarage is :{avarage} and GPA is 3.7")
    elif avarage<=89 and avarage>=87:
        print(f"Student Avarage is :{avarage} and GPA is 3.3")
    elif avarage<=82 and avarage>=80:
        print(f"Student Avarage is :{avarage} and GPA is 2.7")
    elif avarage<=79 and avarage>=77:
        print(f"Student Avarage is :{avarage} and GPA is 2.3")
    elif avarage<=76 and avarage>=73:
        print(f"Student Avarage is :{avarage} and GPA is 2.0")
    elif avarage<=72 and avarage>=70:
        print("GPA is 1.7")
    elif avarage<=69 and avarage>=67:
        print(f"Student Avarage is :{avarage} and GPA is 1.3")
    elif avarage<=66 and avarage>=63:
        print(f"Student Avarage is :{avarage} and GPA is 1.0")
    elif avarage<=62 and avarage>=60:
        print(f"Student Avarage is :{avarage} and GPA is 0.7")
    elif(avarage<60):
        print("Failed")