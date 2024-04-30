s=0
a= int(input("a : "))
b= int(input("b : "))
for i in range(1,a+b):
    if a %i ==0 and b %i ==0:
        if i>s:
            s=i
print(s)