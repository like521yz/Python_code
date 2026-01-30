floods = int(input("请输入金字塔层数:"))

for i in range(1,floods+1):
    # k 控制空格总层数-当前 层数
    for k in range(floods - i):
        print(" ",end="")
    for j in range(2*i-1):
        if j ==0 or j ==2*i-2 or i == floods:
            print("*",end="")
        else:
            print(" ",end="")
    print("")
# for j in range(1,floods+1):
#     for k in range(floods - j):
#         print(" ",end="")
#     for i in range(2*j-1):
#         print("*",end="")
#     print()