n = int(input(" N : "))
p = 0
for i in range(1,n+1):
        print(i,end=' ')
        if i > 9 :
            p += 3
        else :
            p += 2
print()
z = 0
if n > 9:
    z = 6
else :
    z = 5
for j in range(n-2):
    print(1,' '*(p-z),n)
for i in range(1,n+1):
        print(i,end=' ')
        '''elkwfi'''