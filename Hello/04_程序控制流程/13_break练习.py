import random

# print(random.randint(1,100))
count = 0

while True :
    num = random.randint(1, 100)
    if num == 97:
        break;
    count += 1
print(f"生成97一共用了 {count} 次")

