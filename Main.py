# zadanie 1
try:
    a = int(input('Enter number Weekday: '))
    if a == 1:
        print('Monday')
    elif a == 2:
        print('Tuesday')
    elif a == 3:
        print('Wednesday')
    elif a == 4:
        print('Thursday')
    elif a == 5:
        print('Friday')
    elif a == 6:
        print('Saturday')
    elif a == 7:
        print('Sunday')
    else:
        print('input value out of range')
except ValueError:
    print('Error input value')

# zadanie 2
try:
    a = int(input('Enter number day of the month: '))
    if a == 1:
        print('January')
    elif a == 2:
        print('February')
    elif a == 3:
        print('March')
    elif a == 4:
        print('April')
    elif a == 5:
        print('May')
    elif a == 6:
        print('June')
    elif a == 7:
        print('July')
    elif a == 8:
        print('August')
    elif a == 9:
        print('September')
    elif a == 10:
        print('October')
    elif a == 11:
        print('November')
    elif a == 12:
        print('December')
    else:
        print('input value out of range')
except ValueError:
    print('Error input value')

# zadanie 3
try:
    a = float(input('Enter number value: '))
    if a > 0:
        print('Number is positive')
    elif a == 0:
        print('Number is equal to zero')
    elif a < 0:
        print('Number is negative')
    else:
        print('Oops unknown error')
except ValueError:
    print('Error input value')

# zadanie 4
try:
    a = float(input('Enter number value one: '))
    b = float(input('Enter number value two: '))
    if a != b:
        if a < b:
            print(a,b)
        else:
            print(b,a)
except ValueError:
    print('Error input value')
