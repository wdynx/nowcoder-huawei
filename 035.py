# 先写成下三角，再斜着变成上三角

while True:
    try:
        n = int(input())
        res = []
        cur = 1
        for i in range(n):
            res.append([])
            for j in range(i+1):
                res[i].append(cur)
                cur += 1
        for i in range(n):
            cur = []
            for j in range(n-i):
                cur.append(str(res[i+j][j]))
            print(' '.join(cur))
    except:
        break
