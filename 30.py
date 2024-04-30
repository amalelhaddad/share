
n = int(input("enter :"))
for i in range(n):
    id = int(input(" id :"))
    name=str(input(" name :"))
    gender= str(input(" male or female :"))
    m= float(input("m :"))
    a=float(input("mark :"))
    if gender == "male" and m>250:
        print(name)
    if gender== "female"and a>50:
        print(id)
    print(id)

