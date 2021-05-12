"""
Mr. Ashok like to create a flight ticket booking application. To book a
flight, user should enter his / her name, DOB, address and passport
number followed by Start city, destination city and date of travel. Here are
the constraints -
1. Name should be all in upper case and it should be free from special
characters or numbers. His application only allow names of length
ranges from 5 to 30 max.
2. DOB should be in a format of DD-MM-YYYY. Other formats not
allowed.
3. Passport number is only of 8 digits and should start with ‘P’
followed by numbers.
4. Start city and destination city should NOT be same. Here are the
constraints -
1. Start city / End city should be any one of these [ “Paris”,
“Japan”, “China”]
5. Date of travel should be in format [DD-MM-YYYY]
 Write functions to validate all those above constraints and if all validations
successful, return “Flight Ticket Booked”, else return respective error
message. (Example: Invalid Passport number if passport number validation
fails etc….)
"""
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









    
