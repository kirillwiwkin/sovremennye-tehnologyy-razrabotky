# 4
with open("шишкин_кирилл_сергеевич_ум-222_vvod_2.txt", "r") as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

proccess_lambda = lambda x: 0 if x < 0 else 1
proccesed_matrix = [[proccess_lambda(el) for el in rows] for rows in matrix]

print(
f"""Матрица = {matrix}
Обработанная матрица = {proccesed_matrix}""")

with open("шишкин_кирилл_сергеевич_ум-222_vivod_2.txt", "w", encoding="UTF-8") as f:
    f.write(str(proccesed_matrix))
