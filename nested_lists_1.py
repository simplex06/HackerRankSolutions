if __name__ == '__main__':
    students =[]
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = [i[1] for i in students]
    scores = list(sorted(set(scores)))
    res=sorted([i[0] for i in students if i[1]==scores[1]])
    print(*res,sep="\n")