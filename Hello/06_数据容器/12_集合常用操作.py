
#集合常用操作演示

set_a = {"apple", "banana", "orange", "grape", "melon", "kiwi"}
#集合元素个数：len(集合)
print(f"集合set_a的元素个数是：{len(set_a)}")
print("--------------------------------------------------")

#  x in 集合：判断元素是否在集合内
# 判断 apple 是否在集合 set_a 内
print(f"apple 是否在集合 set_a 内：{'apple' in set_a}")
print("--------------------------------------------------")

#集合添加元素：集合.add(元素)
set_a.add("pear")
print(f"向集合 set_a 内添加元素 pear 之后，set_a={set_a}")
print("--------------------------------------------------")

#集合删除元素：集合.remove(元素)
set_a.remove("pear")
print(f"从集合 set_a 内删除元素 pear 之后，set_a={set_a}")
print("--------------------------------------------------")

#从集合中随机删除一个元素：集合.pop()
removed_element = set_a.pop()
print(f"从集合 set_a 中随机删除的元素是：{removed_element}，删除之后，set_a={set_a}")
print("--------------------------------------------------")

#union(集合)：当前集合和指定集合的并集，返回一个新集合
set_b = {"banana", "peach", "watermelon"}
set_union = set_a.union(set_b)
print(f"集合 set_a 和 set_b 的并集是：{set_union}")
print("--------------------------------------------------")

#intersection(集合)：当前集合和指定集合的交集，返回一个新集合
#set_intersection = set_a.intersection(set_b)
set_intersection = set_a & set_b
print(f"集合 set_a 和 set_b 的交集是：{set_intersection}")
print("--------------------------------------------------")

#difference(集合)：当前集合和指定集合的差集，返回一个新集合
#set_difference = set_a.difference(set_b)
set_difference = set_b - set_a
print(f"集合 set_a 和 set_b 的差集是：{set_difference}")
print("--------------------------------------------------")

















