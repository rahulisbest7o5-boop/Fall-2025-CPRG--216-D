print("Leap Year exercise!") 
is_leap_year = False
input_year = int(input("Enter Year: "))
if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False
if is_leap_year:
    print(input_year, "is a leap year")
else:
    print(input_year, "is not a leap year")
 
