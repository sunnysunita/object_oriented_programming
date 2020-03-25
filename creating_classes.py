print("::learn object oriented programming::")


class Student:
    pass


s1 = Student()  # student object, s1
s2 = Student()  # student object, s2

s1.name = "sunny kumar"  # adding attribute to object individually
s1.roll = 79

s2.name = "kamal hasan"
s2.roll = 80

#print(s1.name, s1.roll)  # get attribute value by calling object.attribute
print(s2.name, s2.roll)

print(s1.__dict__)  #getting all attrbutes and values in form of dictionary
print(s2.__dict__)

print(hasattr(s1, "name"))  #hasattr function return True or False, and takes two argument(object,attribute)

print(getattr(s1,"name",""))    #getattr fuction return value of attribute of an object
#print(s1.name)

#delattr(s1,"roll")
print(s1.__dict__)