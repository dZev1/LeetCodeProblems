def lengthOfLastWord(s: str) -> int:
    length = 0
    if (len(s)) == 1:
        return 1
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " " and s[i-1] == " ":
            return length + 1
        if s[i] != " ":
            length += 1
    return length

if __name__ == "__main__":
    a = "a  "
    print(lengthOfLastWord(a))