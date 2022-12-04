students = [{"name":"Tom","id":1,"degree":"d1","active":1},
            {"name":"Sam","id":2,"degree":"d1","active":1},
            {"name":"Mike","id":3,"degree":"d6","active":1},
            {"name":"John","id":4,"degree":"d3","active":0}]
jobs = [{"clerk":[1,3],"lab_admin":[2]}]
assignments = [{"assignment1":[2,3],"assignment2":[1]}]

class Students:
    def __init__(self):
        pass

    def add_student(self, **kwargs):
        max_id = max(students, key=lambda x:x['id'])
        s = {"id": max_id["id"]+1, "active": 1}
        for key,value in kwargs.items():
            s[key] = value
        students.append(s)
        return f"student added successfully with id {int(max_id['id'])+1}"

    def get_student_info(self, student_id):
        ss = [x for x in students if x['id'] == student_id]
        return ss[0] if len(ss) > 0 else "Student not found"

    def delete_student(self, student_id):
        ss = [x for x in students if x['id'] == student_id]
        if len(ss) > 0:
            ss[0]["active"] = 0
            return "student deleted successfully"
        else:
            return "student not found to delete"

    def get_students(self):
        return students

obj = Students()
print(obj.add_student(name="sss", degree="d2"))
print(obj.get_student_info(5))
print(obj.delete_student(5))
print(obj.get_students())