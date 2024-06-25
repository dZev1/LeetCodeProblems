def numJewelsInStones(jewels: str, stones: str) -> int:
    jewel_stone_counter: int = 0
    for stone in stones:
        if stone in jewels:
            jewel_stone_counter += 1
    return jewel_stone_counter


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))
    # OUTPUT: 3
    