


count = 3
for i in range(count):
    name = input("请输入账号：")
    password = int(input("请输入密码："))
    if name != "like" or password != 123:
        print(f"请重新输入账号或密码；您还有{count-1}次机会")
        count -= 1
        if count == 0:
            print("账号已被冻结")
            break;
    else:
        print("恭喜你登录成功")
        break;