n = int(input("enter : "));sum=0;z=0;x=0
for i in range(n):
    a= str(input("enter a: "))
    if a == "فوز":
        sum +=3
        z+=1
    if a== "تعادل":
        sum+=1
    if a == "خسارة":
        x+=1
print(sum)
print(sum/n)
print("مرات الفوز",z)
print("عدد مرات الخسارة",x)
s=(z/n)*100
print(s)
if s>=70:
    print("اداء ممتاز")ٍ
elif 70>s>=50:
    print("اداء جيد")
else:
    print("اداء سيئ")