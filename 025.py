# 按要求顺着来吧

while True:
    try:
        line1 = input().split()
        line2 = input().split()
        n_I, I = int(line1[0]), line1[1:]
        n_R, R = int(line2[0]), line2[1:]
        R = list(set(R))
        R.sort(key=lambda x: int(x))
        res = []
        for target in R:
            cur = []
            for i in range(n_I):
                if target in I[i]:
                    cur.append(str(i))
                    cur.append(I[i])
            if not cur:
                continue
            cur = [target, str(len(cur)//2)] + cur
            res += cur
        res = [str(len(res))] + res
        print(' '.join(res))
    except:
        break
