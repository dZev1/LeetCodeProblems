def isUgly(n: int) -> bool:
    num: int = n
    if num <= 0:
        return False
    for i in [2,3,5]:
        while num % i == 0:
            num = num // i
    return num == 1 


if __name__ == "__main__":
    num = 2147483648
    print(isUgly(num))
    # OUTPUT: True