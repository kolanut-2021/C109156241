do = int(input("輸入度數:"))
s = ns = 0
if do<=120:
    s=do*2.10
    ns=do*2.10
elif do>120 and do<=330:
    s=120*2.10+(do-120)*3.02
    ns=120*2.10+(do-120)*2.68
elif do>330 and do<=500:
    s=120*2.10+210*3.02+(do-330)*4.39
    ns=120*2.10+210*2.68+(do-330)*3.61
elif do>500 and do<=700:
    s=120*2.10+210*3.02+170*4.39+(do-500)*4.97
    ns=120*2.10+210*2.68+170*3.61+(do-500)*4.01
elif do>700:
    s=120*2.10+210*3.02+170*4.39+200*4.97+(do-700)*5.63
    ns=120*2.10+210*2.68+170*3.61+200*4.01+(do-700)*4.50
print("Summer months:"+str(s)+"\n"+"Non-Summer months:"+str(ns))