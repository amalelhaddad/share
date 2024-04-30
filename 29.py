a=7;b=1
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print(" "*a,end="")
    a-=2
    for j in range(b,0,-1):
        print(j,end="")
    b+=1
    if b ==5:
        b=4
    print()
a=1;c=4
for i in range(5,1,-1):
    for j in range(1,i):
        print(j,end="")
    print(" "*a,end="")
    a+=2
    for j in range(c,0,-1):
        print(j,end="")
    c-=1
    print()