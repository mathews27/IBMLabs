import cmath

a = 1
b = int(input("Enter b:"))
c = int(input("Enter c:"))
d = b**2 - (4*a*c)
s1 = (-b-cmath.sqrt(d))/(2*a)
s2 = (-b+cmath.sqrt(d))/(2*a)
print('The solutions are {} and {}'.format(s1, s2))

