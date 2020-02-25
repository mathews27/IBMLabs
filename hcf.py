def hcf(a, b):
    if a < b:
        small = a
    else:
        small = b
    for i in range(1, small+1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf


x = int(input("Enter a:"))
y = int(input("Enter b:"))
print(hcf(x, y))

