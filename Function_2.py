def userName():
    name = input("Enter your Name : ")
    if(name.isupper()):
        if((5<len(name)) and (len(name)<30)):
           DOB()
        else:
            print("Enter valid user nme within the range!!!")
            userName()
    else:
        print("Enter valid name in upper case!!!")
        userName()
def DOB():
    yob = input("Enter YOUR DOB : ")
    dob=[]
    dateob = yob.split("/")
    for i in dateob:
        i = int(i)
        dob.append(i)
    del dateob
        
    if((dob[0]<32) and (dob[1]<13)):
        Pnum()
    else:
        print("Enter DOB in valid format DD/MM/YYYY!!!")
        DOB()
def Pnum():
    passNum = input("enter your passport number : ")
    if((len(passNum)==8) and (passNum[0]=='P')):
        city()
    else:
        print("Enter valid passport number!!!")
        Pnum()

def city():
    startCity = input("Enter your start city : ")
    expect_dest = ["Paris","Japan","China"]
    if(startCity in expect_dest):
        destCity = input("Enter the destination city")
        if(destCity in expect_dest):
            if(startCity != destCity):
                traDate()
            else:
                print("Starting and destination cannot be the same city : ")
                city()
        else:
            print("Enter correct dstination")
    else:
        print("Enter correct destination")
          
def traDate():
    dateTravel = input("enter the date of travel : ")
    travel = []
    dateofTravel = dateTravel.split("/")
    for i in dateofTravel:
        i = int(i)
        travel.append(i)
    del dateofTravel
    if((travel[0]<32) and (travel[1]<13)):
        print("Flight Ticket Booked")
    else:
        print("Enter proper formamat")
        traDate()


userName()









    
