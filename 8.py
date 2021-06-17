a=input("輸入第一行正整數為:")
b=input("第二行中數列中的數字為:").split(" ")
c=[]
for i in range(0,int(a)):
    c.append(b.count(b[i]))

if max(c)==1:
    print("每個數字剛好出現一次")
else:
    d=max(c)
    print("最大出現次數的數字為:",b[c.index(d)])
    print("出現次數為:",d)
