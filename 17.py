a=[]
for i in range(1,11):
    b = int(input("請輸入第"+str(i)+"個數字:"))
    a.append(b)
a.sort(reverse=True)
print("最大的三個數字為:",a[0],a[1],a[2])
a.sort()
print("最小的三個數字為:",a[0],a[1],a[2])