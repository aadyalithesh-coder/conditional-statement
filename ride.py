print("1.car")
print("2.bike")
choice= int(input("Enter your ride:"))

if choice==2:
    print("1.scooty")
    print("2.scooter")
    choice2= int(input("Enter type of bike:"))
    if choice2==1:
        print("You have chosen scooty")
    else:
        print("You have chosen scooter")

elif choice==1:
    print("1.BMW")
    print("2.SUV")
    choice3= int(input("Enter type of car:"))
    if choice3==1:
        print("You have chosen BMW")
    else:
        print("You have chosen SUV")