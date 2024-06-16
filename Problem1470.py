def shuffle(nums: list[int], n: int) -> list[int]:
    list1: list[int] = []
    list2: list[int] = []
    ans: list[int] = []
    
    for i in range(n):
        list1.append(nums[i])
    
    for j in range(n, 2 * n):
        list2.append(nums[j])
    
    for k in range(len(nums)):
        if k % 2 == 0:
            ans.append(list1[int(k /2)])
        else:
            ans.append(list2[int((k - 1) / 2)])
    return ans


if __name__ == "__main__":
    nums = [2,5,1,3,4,7]
    n = 3
    print(shuffle(nums, n))
    # OUTPUT: [2,3,5,4,1,7] 
    