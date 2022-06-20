year = int(input("enter any four digits :"))
if year % 4 ==0:
    if year %100 ==0:
        if year % 400==0:
            print("yes this is leap year")
        else:
         print("not! a leap year")
    else:
        print("yes this is leap year")
else:
     print("NOT IN LEAP YEAR")


