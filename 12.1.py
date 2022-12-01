# 4

n = 223

def digit_sum(n):
    if(int(n / 10) == 0):
        return n
    return n % 10 + digit_sum(int(n / 10))

    
print(digit_sum(n))
    
    
