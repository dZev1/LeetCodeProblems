# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

def addDigits(num: int) -> int:
    string_num = str(num)
    result = 0
    
    for i in range(len(string_num)):
        result += int(string_num[i])

    string_result = str(result)
    
    while len(string_result) >= 2:
        result = 0
        for j in range(len(string_result)):
           result += int(string_result[j])
        string_result = str(result)

    return result

if __name__ == "__main__":
    print(addDigits(38))