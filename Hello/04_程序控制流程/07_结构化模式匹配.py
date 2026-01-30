week = input("今天星期几？")
print(type(week))

match week:
    case"星期一":
        print("今天星期一，猴子穿新衣")
    case"星期二":
        print("今天星期二，猴子当小二")
    case _:
        print("没有匹配的值，默认执行这里的代码")
