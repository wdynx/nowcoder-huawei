while True:
    try:
        p_cnt = 0
        n_cnt = 0
        positive = 0
        ls = list(map(int, input().split()))
        for n in ls:
            if n >= 0:
                p_cnt += 1
                positive += n
            else:
                n_cnt += 1
        print(n_cnt)
        print(round(positive / p_cnt, 1))
    except:
        break
