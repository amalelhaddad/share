n = int(input("enter the number : "))
m=3
for i in range(1,n+1):
    if i == 1:
        for j in range(1,n+1):
            print(j,end=" ")
    elif 1<i<n:
        if n < 9:
            m = n - 5
        if n==10:
            m=3
        if n >=10:
            m+=2
        print(1," "*(n+m),n,end="")
    elif i ==n :
        for j in range(1,n+1):
            print(j,end=" ")
    print()
    '''error'''