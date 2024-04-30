n = int(input("enter the num : "))
x = [0]*n
for i in range(n):
    x[i]=int(input("enter the num : "))
print(x)
# دالة تقوم بأرجاع المتوسط الحسابي للأعداد الموجبة في المواقع الزوجية
def avg(y):
    sum=0
    l=0
    for i in range(len(y)):
        if i %2 ==0 :
          if y[i]>0:
            sum+=1
            l+=y[i]
    avg=sum/l
    print(avg)
avg(x)
#دالة تقوم بارجاع اكبر واصغر قيمة في المصفوفة وموقعها
def max_min(y):
   max=x[0]
   lmax=0
   min=x[0]
   lmin=0
   for i in range (len(x)):
      if max < x[i] :
          max=x[i]
          lmax = i
   print('max v',max, lmax)
   for i in range(len(x)):
       if min>x[i]:
           min = x[i]
           lmin = i
   print('minv',min,lmin)
max_min(x)
#دالة تقوم بضرب مصفوفةفي3 وطبعتها
def mult(y):
     for i in range(len(x)):
          x[i] *= 3
     print(x)
mult()
#دالة تقوم بأرجاع الاعداد الفردية وعددها والاعداد الزوجية وعددها
def even_odd(y):
    o=0
    e=0
    for i in range(len(x)):
        if x[i]%2==0:
            e+=1
            print(x[i])
    print('even',e)
    for i in range(len(x)):
        if x[i]%2!=0:
           o+=1
           print(x[i])
    print('odd',o)
even_odd(x)
#دالة تقوم بترتيب المصفوفة تصاعديا
def sort(y):
     s=sorted(x)
     print(s)
sort(x)