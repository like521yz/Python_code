
list_a = [ele * 2 for ele in range(2,6) ]
print(list_a)
list_b = [ele + ele for ele in "函数"]
print(list_b)

#从键盘循环输入五个成绩
scores = []
for i in range(5):
    score = float(input("请输入成绩:"))
    scores.append(score)
print("成绩情况：",scores)