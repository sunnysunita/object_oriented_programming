class Student:
    def __init__(self,name="No Name",roll="No Rollnumber"):
        self.name=name
        self.roll=roll

s1=Student()
print(s1.__dict__)
s2=Student()
print(s2.__dict__)
s3=Student("Sunny",79)
print(s3.__dict__)
