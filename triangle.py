
class Triangle():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c


    def perimeter (self):
        return self.a + self.b +self.c

    def area (self):
        from math import sqrt
        s = (self.a + self.b + self.c) % 2
        return sqrt(s * (s - self.a) *(s - self.b) * (s - self.c)) 
    
    
    def scale (self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)

    def is_valid (self):
        if self.a + self.b >= self.c and self.b+ self.c >= self.a and self.c + self.a >= self.b:
            return True
        else:
            return False

    def is_right (self):
        if (self.a*self.a+self.b*self.b==self.c*self.c) or (self.c*self.c+self.b*self.b==self.a*self.a) or (self.a*self.a+self.c*self.c==self.b*self.b):
            return True
        else:
            return False



t = Triangle (5,7,8)

print ("Area = %d" % t.area())

print ("Perimeter = %d" % t.perimeter())

print (t.is_right())

print (t.is_valid())

q =t.scale(3)
print (q.a, q.b, q.c)