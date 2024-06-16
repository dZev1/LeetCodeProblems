def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    string1: str = ""
    string2: str = ""
    
    for i in word1:
        string1 += i
    for j in word2:
        string2 += j
    
    return string1 == string2
    
    
if __name__ == "__main__":
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(arrayStringsAreEqual(word1, word2))
    # OUTPUT: True
    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(arrayStringsAreEqual(word1, word2))
    # OUTPUT: False