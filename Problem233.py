def countDigitOne(n: int) -> int:
    counter: int = 0
    i: int = 1
    while i <= n:
        divider = i * 10
        counter += (n // divider) * i
        counter += min(max(n % divider - i + 1, 0), i)
        i *= 10
    return counter

if __name__ == "__main__":
    countDigitOne(824883294)