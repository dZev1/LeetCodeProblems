def TwoSum(nums: list[int], target: int) -> list[int]:
    result: list[int] = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    return []



if __name__ == "__main__":
    nums = nums = [2,5,5,11]
    target = 10
    print(TwoSum(nums, target))