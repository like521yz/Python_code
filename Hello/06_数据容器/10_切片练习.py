
list_name = ["Jack","Lisa","Hsp","Paul","Smith","Kobe"]
#取出前三个名字
list_slice = list_name[0:3:1]
print(list_slice)

#取出后三个名字并保证原来顺序
list_a = list_name[-1:-4:-1]
list_a.reverse()
#list_b = list_a[-1:-4:-1]
print(list_a)