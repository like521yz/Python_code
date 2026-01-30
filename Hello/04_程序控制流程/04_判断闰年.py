num = int(input("请输入一个年份："))
if( num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(f"{num}年是闰年")
else:
    print(f"{num}不是闰年")