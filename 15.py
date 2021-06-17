count=int(input("組數為:"))
count1=[]

for i in range(count):
    count1.append(input("第%d組"%(i+1)).split(" "))

for j in range(count):
    print("第",j+1,"組應收費用:",(int(count1[j][0])*250+int(count1[j][1])*175))