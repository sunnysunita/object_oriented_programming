class Student:
    pp=60
    def student_details(self):
        self.name = "xxx"
        self.roll = 000
        self.marks = 000
    def isPassed(self):
        if self.marks>=Student.pp:
            print(self.name,"is Passed")
        else:
            print(self.name,"is Fail")

s1 = Student()
s1.student_details()
s1.name="Sunny Kumar"
s1.roll=79
print(s1.__dict__)
s1.marks=81
s1.isPassed()


s2=Student()
s2.student_details()
s2.name="kamal"
print(s2.roll)
s2.marks=55
s2.isPassed()

