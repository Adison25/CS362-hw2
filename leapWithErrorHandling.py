print("Program checking to see if a year is a leap year or not")
run = 1
while run == 1:
    year = input("Please enter a year: ") 
    #check input
    if year.isnumeric():
    #if info is valid 
        if int(year) % 4 != 0:
            print(str(year) + " is a common year")
        elif int(year) % 100 != 0:
            print(str(year) + " is a leap year")
        elif int(year) % 400 != 0:
            print(str(year) + " is a common year")
        else:   
            print(str(year) + " is a leap year")
        break
    else:
        print("Please enter an integer!\n")