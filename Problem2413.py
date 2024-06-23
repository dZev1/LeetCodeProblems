def smallestEvenMultiple(n: int) -> int:
    if n % 2 == 0:
        return n
    else:
        return n * 2
        
if __name__ == "__main__":
    print(smallestEvenMultiple(6))