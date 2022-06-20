p = int(input("enter any number of rows:"))
for i in range (1,p+1):
    for j in range(1,p+2-i):
        print("*",end=" ")
    print()