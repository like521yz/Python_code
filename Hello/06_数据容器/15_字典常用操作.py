

#len(字典):返回字典中键值对的数量
dict_a = {"one":1,"two":2,"three":3}
print("字典dict_a的长度为：",len(dict_a))
print("--------------------------------------------------")

#dicrt_a[key]返回key对应的值
print("字典dict_a中key为'two'对应的值为：",dict_a["two"])
print("--------------------------------------------------")

#dict_a[key] = value 向字典中添加键值对
dict_a["four"] = 4
print(f"向字典dict_a中添加键值对'four':4后，dict_a为：{dict_a}")
print("--------------------------------------------------")

#del dict_a[key] 删除字典中指定的键值对
del dict_a["four"]
print(f"删除字典dict_a中key为'four'的键值对后，dict_a为：{dict_a}")
print("--------------------------------------------------")

#key in dict_a:判断key是否在字典中
print(f"key 'three' 是否在字典dict_a中：{'three' in dict_a}")
print("--------------------------------------------------")

#pop(key):删除字典中指定key的键值对，并返回对应的value
removed_value = dict_a.pop("three")
print(f"删除字典dict_a中key为'three'的键值对，其对应的value为：{removed_value}，删除后dict_a为：{dict_a}")
print("--------------------------------------------------")

#keys():返回字典中所有的key
keys = dict_a.keys()
print(f"字典dict_a中的所有key为：{list(keys)}")
print("--------------------------------------------------")

#

#clear():清空字典
dict_a.clear()
print(f"清空字典dict_a后，dict_a为：{dict_a}")
