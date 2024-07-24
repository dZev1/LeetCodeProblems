def getRow(rowIndex: int) -> list[int]:
    def factorial(n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    row: list[int] = []
    for i in range(rowIndex + 1):
        n = factorial(rowIndex) // (factorial(i) * factorial(rowIndex - i))
        row.append(n)
    return row

if __name__ == "__main__":
    rowIndex = 4
    print(getRow(rowIndex))