n=int(input("Enter n:"))
fact = 1
if n<0:
    print("Not have a factorial ")
elif n==0:
    print("The factorial is 1")
else:
    for count in range(1,n+1):
        fact=fact*count
    print(fact)