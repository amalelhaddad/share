z=int(input("enter 1 :"))
x=int(input("enter 2 :"))
y=int(input("enter 3 :"))
h= (x+y+z )/3
if 0<=h<=30:
    print("safrty")
elif 30<h<=60:
    print("madium")
elif 60<h<=100:
    print(("dangerous"))
else:
    print("not of range")

