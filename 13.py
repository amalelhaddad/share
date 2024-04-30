n = int(input("N : "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(n-i):
        print(i,end=" ")
    print()