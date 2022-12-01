# 4
import math

def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)

A = 5
B = 2
C = 3
D = 4

nominator = A*D
denominator = B*C

_gcd = gcd(nominator, denominator)
print(
f"A = {A} B = {B} C = {C} D = {D}")
print(f"Результат деления A/B на C/D: {(nominator/_gcd):g}/{(denominator/_gcd):g}")

# (5/2) / (3/4)
# (5*4) / (2*3)
# 20/6
# 10/3
