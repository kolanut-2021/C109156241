
str = input("請輸入字元為：")
a = len(str)
i = 0
count = 1
while i <= (a/2):
    if str[i] == str[a-i-1]:
        count = 1
        i += 1
    else:
        count = 0
        break
if count == 1:
    print("YES")
else:
    print("NO")