def isSubsequence(s: str, t: str) -> bool:
    counter: int = 0
    i: int = 0
    j: int = 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            counter += 1
            i += 1
        j += 1

        return counter == len(s)


if __name__ == "__main__":
    s: str = "abc"
    t: str = "ahbgdc"
    print(isSubsequence(s,t))
