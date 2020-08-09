# 一开始毫无头绪，直到我写了每行的前4个数。。

dic = {
    0: 3,
    1: 2,
    2: 4,
    3: 2
}
while True:
    try:
        n = int(input())
        if n <= 2:
            print(-1)
        else:
            print(dic[n%4])
    except:
        break
