m = 1
for i in range(8, 0, -1):
    print(i, end=" ")
print()
for i in range(7, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for n in range(1):
        print(m, end=" ")
        m += 1
    print()
for i in range(1, 9):
    print(i, end=" ")
