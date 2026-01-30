month = int(input("请输入月份："))
age = int(input("请输入年龄："))

if 4<month<10:
    if 18<age<60:
        print("票价为：60元")
    elif age>60:
        print("票价为：20元")
    else:
        print("票价为：30元")
else:
    if 18<age<60:
        print("票价为：40元")
    else:
        print("票价为：20元")
