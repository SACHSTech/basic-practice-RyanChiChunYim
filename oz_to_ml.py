oz= float(input("Enter the amount of ounces:"))
people = float(input("Enter the people to serve:"))
oz_to_ml= ((oz*29.57)* people)/4
print("This is how much ml you will need:" + str(oz_to_ml))