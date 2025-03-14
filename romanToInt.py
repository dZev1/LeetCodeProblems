def romanToInt(s: str) -> int:
    roman_int_dict: dict[str,int] = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    n = len(s)
    int_num = 0
    for i in range(n - 1):
        if roman_int_dict[s[i]] < roman_int_dict[s[i + 1]]:
            int_num -= roman_int_dict[s[i]]
        else:
            int_num += roman_int_dict[s[i]]
    int_num += roman_int_dict[s[n - 1]]
    return int_num

if __name__ == "__main__":
    print(romanToInt("MMMDCCCLXXXVIII"))