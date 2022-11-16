from student_info import personalInfo
from departments import software_enginnering,scinceDep
from student_gpa_record import student_gpa
first_name=input("Student first name: ")
last_name=input("Student last name: ")
stu_age=input("Student age : ")
stu_id=int(input("Student Id: "))
has_stu_card=bool(input("Has student card? type' Y or Yes 'for yes and 'N or No' for not: "))
stu_department=input("Enter student department type 'science or sci' or 'software enginnering or sof' or 'pharmacy':  ").lower()
stu_stage=input("Student satge Type 'Freshmen' for first  'Sophomores for second 'Juniors  ' for third and ,'Seniors' for fourth:  ").lower()
    

def student_record():
    
    if (stu_department=="science" ) or (stu_department== "sci"):
        dep="Science Department"
        math_score=int(input("Enter student score in mathmatics: "))
        science_score=int(input("Enter student score in Biology:  "))
        physics_score=int(input("Enter student score in physics: "))
        chemestry_score=int(input("Enter student score in chemestry: "))
        phsycology_score=int(input("Enter student score in phsycology: "))
        
        personalInfo(first_name,last_name,stu_age,stu_id,has_stu_card,dep, stu_stage)
        scinceDep(math_score,science_score,physics_score,chemestry_score,phsycology_score)
        science_materials_list=[math_score,science_score,physics_score,chemestry_score,phsycology_score ]
        student_gpa(science_materials_list)


    elif (stu_department=="software enginnering" ) or (stu_department== "sof"):
        dep="Software Enginering  Department"
        math_score=int(input("Enter student score in mathmatics: "))
        logic_score=int(input("Enter student score in Logic:  "))
        electronic_circuts_score=int(input("Enter student score in  electronic_circuts: "))
        electric_circuitsry_score=int(input("Enter student score in electric_circuits: "))
        human_rights_score=int(input("Enter student score in human_rights: "))
        personalInfo(first_name,last_name,stu_age,stu_id,has_stu_card,dep,stu_stage)
        software_enginnering(math_score,logic_score,electronic_circuts_score,electric_circuitsry_score,human_rights_score)
        software_materials_list=[math_score,logic_score,electronic_circuts_score,electric_circuitsry_score,human_rights_score ]
        student_gpa(software_materials_list)
