"""
格式化输出
"""

name = "张三"
age = 19
score = 65
gender = "男"

# %格式化输出
print("个人信息：%s-%d-%d-%s"%(name,age,score,gender))
# format格式化输出
print("个人信息：{3}-{1}-{2}-{0}".format(name,age,score,gender))
print("个人信息：{0}-{1}-{2}-{3}".format(name,age,score,gender))
# f-strings格式化输出
print(f"个人信息：{name}-{age}-{score}-{gender}")