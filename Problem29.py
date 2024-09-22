def divide(dividend: int, divisor: int):
    n: int = abs(dividend)
    m: int = abs(divisor)
    res: int = 0
    
    while n >= m:
        temp: int = m
        multiplier: int = 1
        while n >= temp:
            n -= temp
            res += multiplier
            multiplier += multiplier
            temp += temp
        
    if (dividend < 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
        return -res
    
    if (res > (2**31 - 1)) or (res < (-(2**31))):
        return (2**31 - 1)
    
    return res
    

if __name__ == "__main__":
    dividend = 10000
    divisor = 3
    print(divide(dividend,divisor))