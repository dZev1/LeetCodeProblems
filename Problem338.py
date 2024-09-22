def countBits(n: int) -> list[int]:
    ans: list[int] = []
    for i in range(n + 1):
        n: str = str(bin(i))
        one_counter: int = 0
        for digit in n:
            if digit == '1':
                one_counter += 1
        ans.append(one_counter)
    return ans

if __name__ == "__main__":
    n = 5
    print(countBits(n))