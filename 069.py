while True:
    try:
        x = int(input())
        y = int(input())
        z = int(input())
        m1 = []
        for i in range(x):
            m1.append(list(map(int, input().split())))
        m2 = []
        for i in range(y):
            m2.append(list(map(int, input().split())))
        m = [[0]*z for _ in range(x)]
        for i in range(x):
            for j in range(z):
                for k in range(y):
                    m[i][j] += m1[i][k]*m2[k][j]
        for line in m:
            print(' '.join(map(str, line)))
    except:
        break
