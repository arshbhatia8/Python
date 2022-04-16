month = input("Enter name of month")

if(month=="February"):
    print("28 Days")
elif(month=="January" or month=="March" or month=="May" or month=="July" or month=="August" or month=="October" or month=="December"):
    print("31 Days")
elif(month=="April" or month=="June" or month=="September" or month=="November"):
    print("30 Days")
else:
    print("Invalid date")
