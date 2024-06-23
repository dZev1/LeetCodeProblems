def GetSum(a:int, b:int) -> int:
    numeros_a: list[int] = []
    numeros_b: list[int] = []
    res: list[int] = []
    for i in range(abs(a)):
        numeros_a.append(0)
    for j in range(abs(b)):
        numeros_b.append(0)
    if a < 0:
        for k in range(len(numeros_a)):
            numeros_b.pop()
        res = numeros_b
    if b < 0:
        for k in range(len(numeros_b)):
            numeros_a.pop()
        res = numeros_a
    if a >= 0 and b >= 0:
        for k in numeros_b:
            res.append(k)
        for k in numeros_a:
            res.append(k)
    return len(res)
    
if __name__ == "__main__":
    a = -1
    b = 1
    
    print(GetSum(a,b))