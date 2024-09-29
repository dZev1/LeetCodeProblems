def isValidAnagram(s: str, t: str) -> bool:
    hashMapS: dict[str, int] = {}
    hashMapT: dict[str, int] = {}

    for letra in s:
        if letra in hashMapS.keys():
            hashMapS[letra] += 1
        else:
            hashMapS[letra] = 1
        
    for letra in t:
        if letra in hashMapT.keys():
            hashMapT[letra] += 1
        else:
            hashMapT[letra] = 1
        
    return hashMapS == hashMapT

if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isValidAnagram(s,t))
    # OUTPUT: True