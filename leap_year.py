year = int(input("Enter the year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{} is a Leap Year'.format(year))
        else:
            print('{} is not a Leap Year'.format(year))
    else:
        print('{} is a Leap Year'.format(year))
else:
    print('{} is not a Leap Year'.format(year))
