def generate(numRows: int) -> list[list[int]]:
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    res: list[list[int]] = []
    row: list[int]
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            n: int = factorial(i) // (factorial(j) * factorial(i - j))
            row.append(n)
        res.append(row)
    return res

if __name__ == "__main__":
    numOfRows = 5
    print(generate(5))
        
        
        