

list_a=[1,23,34,433]
print("列表list_a的长度为：",len(list_a))
list_b=[1,2,3,4]
#将list_a追加到list_b
list_b.extend(list_a)
print("list_b为：",list_b)
#从列表中找到对应值的索引位置
print("1第一次出现在序列的索引为：",list_b.index(1))
#列表翻转
list_a.reverse()
print("翻转后的列表为：",list_a)
#把123插入到index为1的位置
list_a.insert(1,123)
print("list_a",list_a)