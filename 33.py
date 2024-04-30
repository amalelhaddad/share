n = ("احمد يلي درهلي كبدي")
for i in n:
    x=0
    for j in n:
        if i ==j :
            x+=1
    if x>=2 and i !=" ":
        print(i)