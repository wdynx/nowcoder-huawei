# 看看是不是自己结尾

while True:
    try:
        n = int(input())
        cnt = 0
        for i in range(n):
            if str(i**2).endswith(str(i)):
                cnt += 1
        print(cnt)
    except:
        break
