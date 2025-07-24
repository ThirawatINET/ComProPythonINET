def is_armstrong(number):
    digits = str(number)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == number

print(is_armstrong(153))   
print(is_armstrong(9474))
print(is_armstrong(123))   
