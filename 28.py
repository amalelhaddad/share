a=9;b=-1;c=1
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*a,end="")
    a-=2
    for j in range(c,0,-1):
        print(j,end="")
    c+=1
    print()
for i in range(6,0,-1):
    for j in range(i,0,-1):
        if 1==j or j==i:
            print(j,end="")
    print(" "*b,end="")
    b+=2
    for j in range(i,0,-1):
        if 1==j or j==i and i!=6 and j!=1 :
            print("*",end="")
        elif 1!=j or j!=i and i!=6 and j!=1:
            print(" ",end="")
        else:
            print("/")
    print()