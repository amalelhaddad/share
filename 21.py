n = int(input("n :"))
m =n-5
for i in range(1,n+1):
    if i == 1:
        for j in range(1,n+1):
           print(j,end=" ")
    if 1 < i < n:
        print(1," "*(n+m),n,end="")
    if i == n:
        for j in range(1, n + 1):
           print(j,end=" ")

    print()
"""this long, the short in 20"""