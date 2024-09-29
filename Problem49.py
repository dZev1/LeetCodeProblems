def groupAnagrams(strs: list[str]) -> list[list[str]]:
    res: list[list[str]] = []
    hashtable: dict[str, list[str]] = {}
    for word in strs:
        sortedWord: str = ''.join(sorted(word))
        if sortedWord in hashtable.keys():
            hashtable[sortedWord].append(word)
        else:
            hashtable[sortedWord] = [word]
    for key in hashtable.keys():
        res.append(hashtable[key])
    return res
    
    
if __name__ == "__main__":
    strs = ["ddddddddddg","dgggggggggg"]
    print(groupAnagrams(strs))
            