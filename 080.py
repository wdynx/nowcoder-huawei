while True:
    try:
        input()
        ls1 = list(map(int, input().split()))
        input()
        ls2 = list(map(int, input().split()))
        res = set(ls1+ls2)
        print(''.join(map(str, sorted(res))))
    except:
        break
