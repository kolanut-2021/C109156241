
a=int(input("請輸入n："))
b=int(input("請輸入k："))
c=a//b  
if (c>b):
    ans=a+c
    while(c>=b):
        c=c//b
        ans=ans+c
elif(c<b):
    ans=a+c

print("Peter可以抽"+str(ans)+"支紙菸")

