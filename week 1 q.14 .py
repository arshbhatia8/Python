import math
a=int(input("enter x1"))
b=int(input("enter x2"))
c=int(input("enter y1"))
d=int(input("enter y2"))
diffx=(b-a)**2
diffy=(d-c)**2
sum=diffx+diffy
print(math.sqrt(sum))