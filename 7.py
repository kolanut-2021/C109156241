a=input("輸入月租費型式及通話時間為:").split(",")
b=int(a[1])
a=float(a[0])
if a==186:
    b=round(b*0.09)
    if b>=372:
        b=round(b*0.8)
        print("通話費為:",int(b))
    elif b>=186:
        b=round(b*0.9)
        print("通話費為:",int(b))
    else:
        print("通話費為:",int(b))
elif a==386:
    b=round(b*0.08)
    if b>=736:
        b=round(b*0.7)
        print("通話費為:",int(b))
    elif b>=386:
        b=round(b*0.8)
        print("通話費為:",int(b))
    else:
        print("通話費為:",int(b))
elif a==586:
    b=round(b*0.07)
    if b>=1172:
        b=round(b*0.6)
        print("通話費為:",int(b))
    elif b>=586:
        b=round(b*0.7)
        print("通話費為:",int(b))
    else:
        print("通話費為:",int(b))
elif a==986:
    b=round(b*0.06)
    if b>=1972:
        b=round(b*0.5)
        print("通話費為:",int(b))
    elif b>=986:
        b=round(b*0.6)
        print("通話費為:",int(b))
    else:
        print("通話費為:",int(b))