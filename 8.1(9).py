# 4

with open("шишкин_кирилл_сергеевич_vvod.txt", "r") as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

sums = [sum(el) for el in matrix]

max_sum = max(sums)
max_sum_idx = sums.index(max_sum)

min_sum = min(sums)
min_sum_idx = sums.index(min_sum)

print(
f"""Матрица = {matrix}
Строка с максимальным суммой №{max_sum_idx}: {max_sum}
Строка с минимальной суммой №{min_sum_idx}: {min_sum}""")
