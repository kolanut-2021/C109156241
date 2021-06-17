a=input("輸入一個正整數:")
b=[]
d=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)+1):
        b.append(int(a[i:j]))

for i in b:
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        d.append(i)
if d==[]:
    print("No prime found ")        
else:
    print(max(d))