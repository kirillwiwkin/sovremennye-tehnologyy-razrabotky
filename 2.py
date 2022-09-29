import math

x, t = map(int, input("Введите x и t: ").split())
z = (
    (9 * math.pi * t + 10 * math.cos(x)) / (math.sqrt(t) - math.fabs(math.sin(t)))
) * math.pow(math.e, x)

print(f"Z = {z:.2f}")
