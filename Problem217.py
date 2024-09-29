def containsDuplicate(nums: list[int]) -> bool:
    numSet: set = set()
    
    for num in nums:
        if num in numSet:
            return True
        else:
            numSet.add(num)
    return False

if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))
    # OUTPUT: True