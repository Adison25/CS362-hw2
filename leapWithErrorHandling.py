print("Program checking to see if a year is a leap year or not")
year = input("Please enter a year: ")  
if year % 4 != 0:
    print(str(year) + " is a common year")
elif year % 100 != 0:
    print(str(year) + " is a leap year")
elif year % 400 != 0:
    print(str(year) + " is a common year")
else:   
    print(str(year) + " is a leap year")