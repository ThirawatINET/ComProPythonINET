print("Plase select operation")
print("1. Add")
print("2. subtract")
print("3. Multiply")
print("4. divide")
choice = int(input("Select operation form 1,2,3,4: "))
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(f'{num1} + {num2} = {num1 + num2}')
elif choice == 2:
    print(f'{num1} - {num2} = {num1 - num2}')
elif choice == 3:
    print(f'{num1} * {num2} = {num1 * num2}')
elif choice == 4:
        if num2 != 0:
            print(f'{num1} / {num2} = {num1 / num2}')
        elif num1 == 0:
            print(f'{num1} / {num2} = {"0"}')
        elif num2 == 0:
             print(f'{num1} / {num2} = {"0"}')
            