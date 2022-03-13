subject1=int(input("Enter Marks for Subject1 "))
subject2=int(input("Enter Marks for Subject2 "))
subject3=int(input("Enter Marks for Subject3 "))

total = subject1+subject2+subject3
avg=(total)/3
if(avg>90):
  print("Grade=O")
elif(avg>80 and avg<=90):
  print("Grade=A")
elif(avg>70 and avg<=80):
  print("Grade=B")
elif(avg>60 and avg<=70):
  print("Grade=C")
elif(avg>50 and avg<=60):
  print("Grade=D")
elif(avg<=50):
  print("Grade=F")