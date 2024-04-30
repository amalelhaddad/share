y= int(input("enter salary : "))
x =int(input("enter sales : "))
c=0
if x<= 3*y:
  c= y*0.02
if x> 3*y:
    c= y*0.03
if x>5*y:
    c= y*0.05
a = y+c
print("الراتب الاساسي هو : ",a)