color=input("請輸入水果:")
a={"橘子":"橘色","葡萄":"紫色","哈密瓜":"綠色","蘋果":"紅色","香蕉":"黃色"}
if (color in a):
    print(color+"是"+a[color])
else:
    y=input("請輸入顏色:")
    a[color]=y
    print(color+"是"+a[color])