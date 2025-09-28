print("Welcome to my birthday party!")
input("What is your name? ")
age = int(input("How old are you? "))
gender=input("What is your gender? ")
if gender == "male":
    if age >= 18:
        print("You get a free drink and a badge!")
    else:
        print("You get a free drink!")
if age >= 18:
    print("You can enter the party!")
else:
    print("You cannot enter the party!")


elif

