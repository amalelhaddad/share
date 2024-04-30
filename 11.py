n=9
for i in range(1,7):
    for j in range(1,i+1):
        if 1<j<i :
            print(" ",end="")
        else:
            print("*",end="")
    for i in range(n):
        print("5",end="")
    n-=2
    for j in range(1,i+1):
        if i<j<1:
            print("n",end="")
    print()
"""error"""