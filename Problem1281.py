# SUBTRACT THE PRODUCT AND SUM OF DIGITS OF AN INTEGER

def substractProductAndSum(n: int) -> int:
    s = str(n)
    sum = 0
    prod = 1
    
    for i in range(len(s)):
        sum += int(s[i])
        prod *= int(s[i])
    
    return prod - sum

if __name__ == '__main__':
    print(substractProductAndSum(5901))