score = int(input("Enter a test score: "))

while score < 0 or score >100:
    print("Invalid score. Plase enter a score betwwn 0 and 100.")
    score = int(input("Enter your score :"))

print(f"Your score is: {score}")


