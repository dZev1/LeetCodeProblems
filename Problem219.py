def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    hashSet: dict[int,int] = {}

    for i in range(len(nums)):
        if nums[i] in hashSet and abs(i - hashSet[nums[i]]) <= k:
            return True
        else:
            hashSet[nums[i]] = i
    return False

if __name__ == "__main__":
    nums = [1,0,1,1]
    k = 1
    
    print(containsNearbyDuplicate(nums,k))