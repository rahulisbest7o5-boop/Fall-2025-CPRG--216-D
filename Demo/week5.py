
print("Welcome to the average of three numbers program!")
continue_option = 'y'

while continue_option == 'y':
    print("Please enter the number three number x,y,z")
    x = float(input("\n"))
    y = float(input("\n"))
    z = float(input("\n"))
    average = (x + y + z) / 3
    print(f"The average is: {average}")

    user_input = input("Do you want to continue? (y/n)")
  