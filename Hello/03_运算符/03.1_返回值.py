# 0为false
# 非0为true
a = 0
b = 3
# and：返回最后一个为false的操作数 如果所有操作数都为true，则返回最后一个操作数
result = a and b
print(result)

# or: 返回第一个为true的操作数 如果所有操作数都为false, 返回最后一个操作数
result = a or b
print(result)

result = a or False
print(result)