number = int(input("Enter the number:"))

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print('{} is not a prime number'.format(number))
            break
    else:
        print('{} is a prime number'.format(number))
else:
    print('{} is not a prime number'.format(number))
