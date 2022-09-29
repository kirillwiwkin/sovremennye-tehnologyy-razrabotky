a, b = map(int, input("Введите A и B: ").split())

for i in range(a, b - 1, -1):
    if i % 2 != 0:
        print(i)
