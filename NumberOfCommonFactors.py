def commonFactors(a: int, b: int) -> int:
    common_factors = []
    
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)

    return len(common_factors)

if __name__ == "__main__":
    print(commonFactors(25,30))
    