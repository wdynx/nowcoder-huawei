from collections import Counter
while True:
    try:
        input()
        names = input().split()
        input()
        votes = input().split()
        cnt = Counter(votes)
        for key in names:
            print(key, ':', cnt[key])
        print('Invalid :', len(list(filter(lambda x: x not in names, votes))))
    except:
        break
