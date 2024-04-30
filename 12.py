n =int(input("enter number : "));a=1;b=1
for i in range(1,n+1):
    x=1
    for j in range(1,n+1):
        if i==a and j==x :
            print(a,end="")
            print(" ",end="")
        if i ==x and j ==a:
            print(a, end="")
            print(" ", end="")
            b+=1
        x += 1
    a+=1
    print()
    """error"""