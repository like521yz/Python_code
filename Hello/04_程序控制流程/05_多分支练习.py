height = float(input("请输入身高(cm)："))
wealth = float(input("请输入财富(万)："))
handsome = input("是否为帅哥(\'是\'或\'不是\')：")
if height >= 180 and wealth >=1000 and handsome == "是":
    print("我一定要嫁给他！！！")
elif height >= 180 or wealth >=1000 or handsome == "是":
    print("嫁吧,总比没有的强。")
else:
    print("坚决不嫁！！！")