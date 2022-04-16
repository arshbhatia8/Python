pd=input("enter a passsword")
length=len(pd)
digit=alphabet=char=0
ch='$','#','@'
if length<6 and length>16:
    print("Not a Valid Password")
else:  
    for i in pd:
        if(i.isdigit()):
            digit=digit+1
        elif(i.isalpha()):
            alphabet=alphabet+1
        elif  i == ch:
            char=char+1
    if digit>0 or alphabet>0 or char>0:
        print("Valid Password")
    else:
        print("Not a Valid Password")