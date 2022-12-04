students = [{"name":"Tom","id":1,"degree":"MCA"},
            {"name":"Sam","id":2,"degree":"B.Tech"},
            {"name":"Mike","id":3,"degree":"BCA"},
            {"name":"John","id":4,"degree":"M.Sc"}]
functions = {"studying":[1,2,3],"reading":[2,4],"playing":[3]}
jobs = {"Intern":[1,3],"Student":[2]}
assignments = {"Python":[2,3],"DB":[1]}

def getStudentFunctions(id):
    sname = [x["name"] for x in students if x["id"] == id]
    if len(sname)>0:
        print(f"student name is:{sname[0]}")
        stuFun = [ key for key,value in functions.items() if id in value ]
        return f'{sname[0]} functions are: {",".join(stuFun)}'
    else:
        return "student not found"

def addStudentFunction(funcName, studentId):
    if funcName in functions.keys():
        if studentId not in functions[funcName]:
            functions[funcName].append(studentId)
        else:
            return 'already member of the function'
    else:
        functions[funcName] = [studentId]
    return 'student added successfully'

def getStudentJobs(id):
    sname = [x["name"] for x in students if x["id"] == id]
    if len(sname)>0:
        print(f"student name is:{sname[0]}")
        stuFun = [ key for key,value in jobs.items() if id in value ]
        return f'{sname[0]} jobs are: {",".join(stuFun)}'
    else:
        return "student not found"

def getStudentAssignments(id):
    sname = [x["name"] for x in students if x["id"] == id]
    if len(sname)>0:
        print(f"student name is:{sname[0]}")
        stuFun = [ key for key,value in assignments.items() if id in value ]
        return f'{sname[0]} assignments are: {",".join(stuFun)}'
    else:
        return "student not found"
def addStudent(**kwargs):
        
    maxid=0
    for g in students:
        if g["id"]>maxid:
            maxid = g["id"]
    print(maxid)
    s={"id":maxid+1}
    for key,value in kwargs.items():
        s[key]=value
        
    students.append(s)
    return f"student added successfully with to {students}"
