def numberOfBeams(bank: list[str]) -> int:
    prev: int = 0
    res: int = 0
    curr: int = 0 
    for laser in bank[0]:
        if laser == "1":
            prev += 1
    for i in range(1,len(bank)):
        curr = 0 
        for laser in bank[i]:
            if laser == "1":
                curr += 1
        if curr > 0:
            res += prev * curr
            prev = curr
    return res

if __name__ == "__main__":
    bank = ["011001",
            "000000",
            "010100",
            "001000"]
    
    print(numberOfBeams(bank))
    # OUTPUT: 8
