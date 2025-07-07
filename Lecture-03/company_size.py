employees = int(input('Enter the number of employees: '))

if employees < 50:
    print('This is a small company .')
elif employees < 250:
    print('This is a medium-sized company .')
elif employees >= 250:
    print('This is a large company .')