n = int(input("enter the number : "))
for i in range(1,n):
    for j in range(1,i+1):
        if 1<j<i and j<=10:
            print(" ",end=" ")
        elif 1 < j < i:
            print("  ", end=" ")
        else:
            print(j,end=" ")
    print(" ")
for i in range(1,n+1):
    print(i,end=" ")