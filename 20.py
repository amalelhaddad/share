n = int(input("N : "))
for i in range(1,n+1):
    if i ==1 or i ==n:
        for j in range(1,n+1):
            print(j,end=" ")
    else:
        for j in range(1,n+1):
            if j ==1 or j ==n:
                print(j,end=" ")
            else:
                print(" ",end=" ")
    print()
