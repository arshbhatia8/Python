strin=input("enter the string")
digit = alphabet = 0
for i in strin:
    if(i.isdigit()):
        digit=digit+1
    elif (i.isalpha()):
        alphabet=alphabet+1
print("no. of digits are ",digit)
print("no. of letters are ",alphabet)