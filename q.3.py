a = int(input("Enter the Number: "))
if(a==2):
 number = int(input ("Enter the number to print the multiplication table: "))      
 print ("The Multiplication Table of: ", number)    
 for count in range(1, 11):      
   print (f"{number}x{count}={number*count}")    

if(a==1):
    print("Fibonacci sequence:")
    nterms=20
    count=0
    n1, n2 = 0, 1
    while count < nterms:
       print(n1, end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1