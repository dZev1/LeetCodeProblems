def findGCD(nums: list[int]) -> int:
    common_factors: list[int] = []
    
    a: int = min(nums)
    b: int = max(nums)
    
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            common_factors.append(i)
    
    return common_factors[len(common_factors) - 1]

if __name__ == "__main__":
    nums = [2,5,6,9,10]
    print(findGCD(nums))
    # OUTPUT: 2