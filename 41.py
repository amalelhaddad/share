x=int(input("enter : "))
a=[0]*x
for i in range(0,x):
    a[i]=int(input(" "))

s=0
for i in range(0,x):
    if i %2==0:
        if a[i]>0:
            s+=a[i]
y=s/x
print(y)
print("--------")
d=0
for i in range(0,x):
    if i<=x/2:
        d+=a[i]
n=d**2
print(n)