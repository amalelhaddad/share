n = int(input("N : ")); a=0 ; b=0 ; c=0
for i in range(1,n+1):
    if i %2 ==0:
        a+=i

        print(i)
    if i %2 !=0:
        b+=i
    x=0
    for j in range(1,n+1):
        if i %j ==0:
            x+=1
    if x <=2:
        c+=i
print(a,b,c)