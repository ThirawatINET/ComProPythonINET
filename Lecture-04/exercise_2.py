keep_going = "y"

while keep_going.lower() == "y":
    cost = float(input("Enter the item's wholesale cost: "))
    allprice = cost * 2.5
    print(f"Retail price: ${allprice:.2f}") 
    keep_going = input("Do you want to continue (y/n):")