name_valid = False 
while name_valid == False :
    #Ask user to input their full name.
    name = input("Please enter your full name: ")
    name = name.strip(" ")

    #Perform some validation to check the user has entered a full name.
    if name == (""):
        print("You haven't entered anything")

    elif " " not in name:
        print("You must enter a full name")

    elif len(name) < 4:
        print("Your name is too short")
        
    elif len(name) > 25:
        print("Your name is too long")

    else:
        print("Thank you for entering your name")
        name_valid = True
