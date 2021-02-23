if __name__ == '__main__':
    records = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    second = sorted(list(set([score for name, score in records])))[1]
    for name,score in sorted(records):
          if score == second:
              print(name)