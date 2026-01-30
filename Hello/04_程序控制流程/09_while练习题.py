
i = 1
while i <= 100:
    if i%3==0:
        print(i)
    i += 1

# 打印偶数
num = 40
num2 = 0
num3 = 0
while num<200:
    if num % 2 == 0:
        print(f"{num}")
        num2 += 1
        num3 +=num
    num += 1
print(f"偶数个数为{num2}；总和为{num3}")