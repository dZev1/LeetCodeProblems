def encode(strs: list[str]) -> str:
    res: str = ""
    for word in strs:
        res += str(len(word)) + "#" + word
    return res

def decode(s: str) -> list[str]:
    res: list[str] = []
    i: int = 0
    
    while i < len(s):
        j: int = i
        while s[j] != "#":
            j += 1
        n: int = int(s[i:j])
        res.append(s[j + 1 : j + 1 + n])
        i = j + 1 + n
    return res

if __name__ == "__main__":
    strs = ["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"]
    print(encode(strs))
    print(decode(encode(strs)))