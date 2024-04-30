a=13;b=8;s=1;n=2
for i in range(1,8):
    print(" "*i,i," "*a,b)
    a-=2;b-=1
print(" "*9,"1")
for i in range(7,0,-1):
    print(" "*i,i," "*s,n)
    s+=2;n+=1