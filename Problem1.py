# def TwoSum(nums: list[int], target: int) -> list[int]:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if (nums[i] + nums[j]) == target:
#                 return [i, j]

# TIME COMPLEXITY : O(n^2)
# SPACE COMPLEXITY: O(1)

def TwoSum(nums: list[int], target: int) -> list[int]:
    hashTable: dict[int,int] = {}
    for i in range(len(nums)):
        diff: int = target - nums[i]
        if diff in hashTable:
            return [hashTable[diff], i]
        hashTable[nums[i]] = i

# TIME COMPLEXITY : O(n)
# SPACE COMPLEXITY: O(n)


if __name__ == "__main__":
    nums = nums = [2,5,5,11]
    target = 10
    print(TwoSum(nums, target))