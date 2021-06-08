"""
Create a class Student with parameterised constructor name and gender. Create a getter which 
returns name in the format Mr. <<name>> if the gender is Male, Ms. <<name>> if the gender is 
Female.
"""
class student:
    def __init__(self,name,gender):
         self._name = name
         self._gender = gender

    def gen_check(self):
        if(self._gender =="Male" ):
            return "Mr."+self._name
        else:
            return "Ms."+self._name

f =student("john","male")
print(f.gen_check())
