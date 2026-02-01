#集合生成式用{}表示；列表生成式用[]表示

set_a = {ele *2 for ele in range(1,6)}
print(f"集合 set_a 中的元素是：{set_a}")
print("--------------------------------------------------")

set_b = {ele + ele for ele in "like"}
print(f"集合 set_b 中的元素是：{set_b}")