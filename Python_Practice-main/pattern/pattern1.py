pattern =int (input("enter any number of rows:"))
for i in range (pattern,0,-1):
    for j in range(1,i+1):
        print("#",end=" ")
    print()