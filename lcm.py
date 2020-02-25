def lcm(a, b):
    if a > b:
        big = a
    else:
        big = b
    while True:
        if big % a == 0 and big % b == 0:
            number = big
            break
        big += 1
    return number


x = int(input("Enter a:"))
y = int(input("Enter b:"))
print('The L.C.M of two numbers are', lcm(x, y))
