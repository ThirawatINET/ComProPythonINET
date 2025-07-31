heroes = ["Ironman", "Thor", "Hulk", "Spiderman",]
print("1.Display Heroes")
print("2.Add Heroes")
print("3.Insert Heroes")
print("4.Remove Heroes")
print("5.Display Sorted Heroes(Ascemding / Descending)")
hero = int(input("Choose your way: "))

def Display_Heroes():
    print(heroes)

def Add_Heroes():
    name = input("Enter hero name to add: ")
    heroes.append(name)
    print(name, "added.")
    print(heroes)

def Insert_Heroes():
    heroes.insert(4,"Hanuman")
    print(heroes)

def Remove_Heroes():
    heroes.remove("Ironman")
    print(heroes)

def sort_Heroes():
    order = input("Ascemding (A) or Descending (D): ")
    if order == 'A':
        print(heroes[1::])
    elif order == 'B':
        print(heroes[::-1])



if hero == 1:
    Display_Heroes()
elif hero == 2:
    Add_Heroes()
elif hero == 3:
    Insert_Heroes()
elif hero == 4:
    Remove_Heroes()
elif hero == 5:
    sort_Heroes()


    



  
    





    


    

   
