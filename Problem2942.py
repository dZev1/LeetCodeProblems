def findWordsConatining(words: list[str], x: str) -> list[int]:
    result: list[int] = []
    for i in range(len(words)):
        if x in words[i]:
            result.append(i)
    return result


if __name__ == "__main__":
    words = ["leet","code"]
    x = "e"
    print(findWordsConatining(words,x))
    # Output: [0,1]