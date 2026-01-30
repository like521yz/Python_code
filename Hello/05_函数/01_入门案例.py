
def cry():
    print("正在调用函数cry")

# cry()

def sum1():
    sum = 0
    for i in range(1,1001):
        sum += i
    print(f"和为{sum}")
# sum1()

def sum2():
    num = int(input("请输入一个数"))
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(f"和为{sum}")
# sum2()

# 计算两数之和
def sum3(a,b):
    return  a + b

result = sum3(4,5)
print(f"a+b={result}")