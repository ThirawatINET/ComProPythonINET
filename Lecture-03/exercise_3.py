hours_worked =  int(input("Enter the number of house worked: "))
pay_rate = int(input("Enter the hourly pay rate: "))
if hours_worked >40:
    gross_pay = ((hours_worked -40)*1.5*pay_rate) + (40 * pay_rate)
    print(gross_pay)

    