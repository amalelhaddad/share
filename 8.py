n = int(input("عدد المواد :"))
Sum = 0
for i in range(n):
    n = str(input("اسم الصنف :"))
    q = int(input("عدد الوحدات :"))
    unit_price = float(input("سعر الوحدة :"))
    Sum += q*unit_price
print("السعر الاجمالي: ", Sum)
if 25000 < Sum < 50000:
    Sum *= 0.9
if 50000 < Sum < 100000:
    Sum *= 0.85
if Sum > 100000:
    Sum *= 0.8
print("لسعر الصافي ", Sum)
