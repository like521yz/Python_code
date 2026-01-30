

str_a = "jack like tom hsp tom"
print(f"字符串{str_a}，有{len(str_a)}个zifu")
#replace返回字符串副本
str_a_new = str_a.replace("jack","杰克",1)
print(f"str_a_new= {str_a_new }")
print(f"str_a: {str_a}")
#split:返回一个有字符串组成的列表
str_a_split = str_a.split(" ")
print(f"str_a_spli={str_a_split}；类型是：{type(str_a_split)}")
print(f"str_a: {str_a}")
#count统计tom在字符串中出现的次数
print("tom在字符串中出现的次数",str_a.count("tom"))
#index:从字符串中找出指定字符串第一个匹配项的索引
print("tom第一次出现的索引为",str_a.index("tom"))
#strip移除其字符串前后的空格或其他字符串



str_b = "123like321"
str_b_strip = str_b.strip("132")
print(f"str_b_strip= {str_b_strip}")
print(f"str_b={str_b}")

#lower返回字符串小写的副本
str_c = "DaTa"
str_c_lower = str_c.lower()
print(f"str_c_lower= {str_c_lower}")
print(f"str_c= {str_c}")

#upper返回字符串大写的副本
str_d = "like"
str_d_upper = str_d.upper()
print(f"str_d_upper= {str_d_upper}")
print(f"str_d= {str_d}")
