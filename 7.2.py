# 4

points = [
    (1,2),
    (2,3),
    (3,4),
]

x = 1
y = 1
r = 2

def is_in_circle(p):
    global x,y,r
    a,b = p
    if (x-a)*2 + (y-b)**2 <= r**2:
        return True
    else:
        return False

print(f"Точек в окружности: {sum(1 for p in points if is_in_circle(p))}")



