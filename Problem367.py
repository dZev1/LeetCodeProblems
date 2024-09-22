def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    for i in range(num):
        if i * i == num:
            return True
    return False

if __name__ == "__main__":
    num = 1
    print(isPerfectSquare(num))