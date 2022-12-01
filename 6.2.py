# 4

array = [1,6,6,0,-3,9,2,-1,0]

odd_only = [el for el in array if el % 2 != 0]

print(f"Массив {array}")

if odd_only:
    print(f"Нечетные в обратном порядке: {odd_only[::-1]}")
else:
    print("В массиве нет нечетных чисел")
