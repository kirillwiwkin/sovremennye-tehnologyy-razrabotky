# 4

def is_prime(n, div=3):
    if n <= 1:
        return False
    elif div >= n:
        return True
    elif n % div == 0:
        return False
    else:
        return is_prime(n, div+1)
    

print(is_prime(7))
