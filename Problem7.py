def reverse(x: int) -> int:
        x_str: str = str(abs(x))
        length = len(x_str)
        reversed_number_str: str = ""
        reversed_number: int = 0
        for i in range(length):
            reversed_number_str += x_str[length - 1 - i]
        
        reversed_number = int(reversed_number_str)
        
        if reversed_number < -2**31 or reversed_number > (2**31 - 1):
            return 0
        if x < 0:
            return reversed_number * (-1)
        else:
            return reversed_number
    
    
if __name__ == "__main__":
    print(reverse(1534236469))
    print(1534236469 > (2**31 - 1))