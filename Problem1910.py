def removeOccurrences(s: str, part: str) -> str:
    test: bool = True
    while test:
        test = False
        i: int = s.find(part)
        if i != -1:
            s = s[:i] + s[i + len(part):]
            test = True
    return s


if __name__ == "__main__":
    s: str = "aabababa"
    part: str = "aba"
    
    print(removeOccurrences(s,part))
    # Output: "dab"