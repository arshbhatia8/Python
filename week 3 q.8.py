class Triangle:
    def __init__(self,a, b, c):
        self.a = 3
        self.b = 4
        self.c = 5
 
    def Triangle_perimeter(self):
        perimeter = 3+4+5
        return (self.a+self.b+self.c)    
    def Triangle_area(self):
        s = (self.a + self.b + self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
obj = Triangle(3,4,5)
print("Area of triangle : {}".format(obj.Triangle_area()))
print("Perimeter of triangle : {}".format(obj.Triangle_perimeter()))