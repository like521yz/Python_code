
class_num = 5
student_num = 4

total = 0.0
pass_num = 0
for j in range(class_num):
    sum = 0.0
    for i in range(student_num):
        score = float(input(f"请输入{j+1}班第{i+1}个同学的成绩："))
        sum += score
        if score>=60:
            pass_num += 1
    total += sum
    print(f"第{j+1}个班级的平均分为：{sum/student_num};及格人数为：{pass_num}")
print(f"三个班的平均分为{total/class_num}及格人数为：{pass_num}")

