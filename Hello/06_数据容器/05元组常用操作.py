
tuple_a = (100,200,300,400,600,300)
#符合要求的数据在元组中第一次出现索引
print("300第一次出现的索引",tuple_a.index(300))
#元组长度
print("tuple_a长度为：",len(tuple_a))
print("tuple_a最大数为：",max(tuple_a))
print("tuple_a最小数为：",min(tuple_a))

#数据在元组中出现的次数
print("300出现的次数为：",tuple_a.count(300))
print("100出现的次数为：",tuple_a.count(100))
