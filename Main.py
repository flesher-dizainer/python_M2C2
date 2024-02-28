#zadanie 1
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
except Exception:
    print('Error input value')

#zadanie 2