def isThree(n: int) -> bool:
    divisors: list[int] = [1, n]
    curr_divisor: int = 2
    
    while curr_divisor < n:
        if n % curr_divisor == 0:
            divisors.append(curr_divisor)
        curr_divisor += 1

    return len(divisors) == 3

if __name__ == "__main__":
    n = 10
    print(isThree(n))