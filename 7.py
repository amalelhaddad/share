def m (a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] %2 ==1:
                a.remove(a[i][j])
                a.insert(0,a[i][j])
    return a

a=[[ 5, 43, 4, 8],
   [75,92,27,72],
   [81, 8,84,28],
   [52,92,88,93],
   ]

m(a)
print(a)