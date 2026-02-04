
#字典的创建
#空字典
dict_empty = {}
dict_empty2 = dict()

#key是唯一的，不可重复
dict_a = {"name":"jack","age":18}
print("名字为：", dict_a["name"])
#字典不支持索引 会报错
#print("字典dict_a的第0个元素为：", dict_a[0])  # 会报错

#遍历字典
#只获取key
for key in dict_a:
    print(f"key={key}")
#只获取value
for value in dict_a.values():
    print(f"value={value}")
#同时获取key和value
for key,value in dict_a.items():
    print(f"key={key}，value={value}")