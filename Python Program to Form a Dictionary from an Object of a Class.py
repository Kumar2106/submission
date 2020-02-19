class student():
    def __init__(self,name,department,rollno):
        self.name = name
        self.department = department
        self.rollno = rollno
student1 = student("kumar Aditya","B.voc",12)
print(student1.__dict__)