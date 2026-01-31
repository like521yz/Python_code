#字符串切片
str_a = "Hello World"
str_slice = str_a[0:5:2]
print(str_slice)

#列表切片取“tom”“like”
list_a = ["jack","tom","nono","like","yoyo"]
list_slice = list_a[1:4:2]
print(list_slice)

#元组切片取3000，4000
tuple_a = (100,200,3000,4000,50,40)
tuple_slice = tuple_a[2:4:1]
print(tuple_slice)

#逆序切片
str_a_slice = str_a[-1::-2]
print(str_a_slice)
