a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if(a>=b and a>=c):
    large=a
if(b>=a and b>=c):
    large=a
else:
    large=c
print(large)