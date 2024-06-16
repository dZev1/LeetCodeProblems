def sortTheStudents(score: list[list[int]], k: int) -> list[list[int]]:
    kth_scores: list[int] = []
    res: list[int] = []
    
    for i in range(len(score)):
        kth_scores.append(score[i][k])
    
    kth_scores.sort(reverse = True)
    
    while len(res) != len(score):
        for j in range(len(score)):
            for l in range(len(kth_scores)):
                if kth_scores[l] == score[j][k]:
                    res.append(score[l])
            
    return res

if __name__ == "__main__":
    notes = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
    n = 2
    print(sortTheStudents(notes, n))
    # OUTPUT: [[7,5,11,2],[10,6,9,1],[4,8,3,15]]
    
