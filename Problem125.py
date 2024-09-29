def isPalindrome(s: str) -> bool:
    s_no_spaces = ""
    a = s.lower()
    for letter in a:
        if letter.isalnum():
            s_no_spaces += letter
    return s_no_spaces == s_no_spaces[::-1]

if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(isPalindrome(s))
    