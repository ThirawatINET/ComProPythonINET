try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator "))
    result = numerator / denominator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zeo.")
except ValueError:
    print("Error: Invalid input.. Please enter numberic valu")
finally:
     print("Execution completed, wheter an exception occurred or not")

print("End of program")