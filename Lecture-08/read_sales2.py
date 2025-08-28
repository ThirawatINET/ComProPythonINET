with open("sales.txt", "r") as sales_file:
    for line in sales_file:
        amoount = float(line)
        print(f"{amoount:.2f}")