medical=input("Do you have a medical condition(Y/N:)").upper()
if medical=="Y":
    print("you are allowed")
else:
    atten=int(input("Enter attendence number:"))
    if atten>=75:
        print("you are allowed")
    else:
        print("you are not allowed")

    
