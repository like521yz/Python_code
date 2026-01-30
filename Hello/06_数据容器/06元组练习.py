
tuple_a = ('大话西游','周星驰',80,['周星驰','小甜甜'])
print("票价索引为：",tuple_a.index(80))

del tuple_a[3][1]
tuple_a[3].append('牛魔王')
tuple_a[3].append('猪八戒')
for i in tuple_a[3]:
    print(i)
