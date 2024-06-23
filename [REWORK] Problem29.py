def divide(dividend: int, divisor: int):
    n = dividend
    
    if divisor == -1:
        return -n
    if divisor > 0:
        while n > divisor:
            if n - divisor < divisor:
                return n - (n - divisor)
            else:
                n -= divisor
    if divisor < 0:
        while n > 0:
            n += divisor
    return n

if __name__ == "__main__":
    dividend = 10
    divisor = 3
    print(divide(dividend,divisor))