n=0
while True:
    a= str(input("enter : "))
    if a!="0":
        n+=1
    if a=="0":
        break
if n > 5:
    n*= 3
else:
    n*=5
print(n)