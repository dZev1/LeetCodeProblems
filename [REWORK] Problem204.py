def CountPrimes(n: int) -> int:
    counter: int = 0
    is_prime: bool
    for i in range(n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime and i not in [0, 1]:
            counter += 1
    return counter

if __name__ == "__main__":
    n = 4999779
    print(CountPrimes(n))
    # OUTPUT: 4