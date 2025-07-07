inchar = input("input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put Uppercase Letter ", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put Lowercase Letter ", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You in put Number ", inchar)
else :
     print("It's not a letter or number.", inchar)
