def get_students_marks():
    total = mark1+mark2+mark3
    return total

def get_student_grade():
    if((mark1+mark2+mark3)>50):
        return "A"
    else:
        return "B"

def validate_marks():
    if(mark1,mark2,mark3 < 0 ):
        return False
    if(mark1,mark2,mark3 > 25):
        return False
    else:
        return True

def validate_student_name():
    if((5<len(name)) and (len(name)<25)):
        return True
    else:
        return False
        
name = input("Enter Your Nmae : ")
mark1 = int(input("Enter the Mark1 : "))
mark2 = int(input("Enter the Mark2 : "))
mark3 = int(input("Enter the Mark3 : "))
print(get_students_marks())
print(get_student_grade())
print(validate_marks())
print(validate_student_name())




    
