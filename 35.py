n = str(input("n : "))
a=0
for i in n:
    a+=1
for i in n:
    if a ==3:
        if i == "1":
            print("مائة ")
        if i == "2":
            print("مئتان")
        if i == "3":
            print("ثلاثمائة")
        if i == "4":
            print("اربعمائة")
        if i == "5":
            print("خمسمائة")
        if i == "6":
            print("ستمائة")
        if i == "7":
            print("سبعمائة")
        if i == "8":
            print("ثمانمائة")
        if i == "9":
            print("تسعمائة")
        a-=1
        if a == 2:
            if i == "1":
                z="عشر"
            if i == "2":
                z=("عشرون")
            if i == "3":
                z=("ثلاثون")
            if i == "4":
                z=("اربعون")
            if i == "5":
                z=("خمسون")
            if i == "6":
                z=("ستون")
            if i == "7":
                z=("سبعون")
            if i == "8":
                z=("ثمانون")
            if i == "9":
                z=("تسعون")
            a-=1
            if a==1:
                if i =="1":
                    print("واحد")
                if i =="2":
                    print("اثنين")
                if i =="3":
                    print("ثلاثة")
                if i =="4":
                    print("اربعة")
                if i =="5":
                    print("خمسة")
                if i =="6":
                    print("ستة")
                if i =="7":
                    print("سبعة")
                if i =="8":
                    print("ثمانية")
                if i =="9":
                    print("تسعة")
            print(z)