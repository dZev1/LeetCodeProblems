# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.

# INPUT: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# OUTPUT: 6

def maximum(lista: list[int]) -> int:
    curr_max: int = lista[0]
    
    for i in lista:
        if i > curr_max:
            curr_max = i
    return curr_max

def mostWordsFound(sentences: list[str]) -> int:
    sentences_lengths: list[int] = []
    
    for i in sentences:
        sentences_lengths.append(len(i.split()))
    
    return maximum(sentences_lengths)

    
if __name__ == "__main__":
    sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
    print(mostWordsFound(sentences))
    # OUTPUT: 6