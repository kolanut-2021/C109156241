m=int(input("請輸入階乘值M:"))
s=1
n=0
while s<=m:
    n+=1
    s*=n
    
print("超過M為",m,"的最小階乘N值為:",n)