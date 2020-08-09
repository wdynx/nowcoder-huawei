while True:
    try:
        n = int(input())
        ls = list(map(int, input().split()))
        ls.sort(reverse=bool(int(input())))
        print(' '.join(map(str, ls)))
    except:
        break
