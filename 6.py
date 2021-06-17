'''  輸入說明:1<=N<=7，輸入值為1,3,9,5,7按ENTER。 '''
a=input("輸入值為:").split(",")
a=sorted(a)
a="".join(a)
b=a[::-1]
print("最大值數列與最小值數列差值為",int(b)-int(a))