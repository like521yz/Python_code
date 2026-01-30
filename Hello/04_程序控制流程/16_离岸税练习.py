money = 100000
count = 0
while True:
    if money > 50000:
        money -= money * 0.05
        count += 1
    elif money >= 1000:
        money -= 1000
        count += 1
    else:
        break;
print(f"该人可以过{count}次")



