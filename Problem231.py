def isPowerOfTwo(n: int) -> bool:
    while n % 2 == 0 and n != 1 and n != 0:
        n /= 2
    return n == 1

if __name__ == "__main__":
    n = 12
    print(isPowerOfTwo(n))