def topKFrequent(nums: list[int], k: int) -> list[int]:
    res: list[int] = []
    hashtable: dict[int, int] = {}
    for num in nums:
        if num in hashtable.keys():
            hashtable[num] += 1
        else:
            hashtable[num] = 1
    for i in range(k):
        res.append(max(hashtable, key = hashtable.get))
        for key in hashtable.keys():
            if key == res[i]:
                hashtable[key] = -1
    return res


print(topKFrequent([1,1,1,2,2,3], 2))