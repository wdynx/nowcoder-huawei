# 实在找不出规律来，直接暴力遍历吧

while True:
    try:
        n = int(input())
        cnt = 0
        for i in range(1, n+1):
            if i%7 == 0 or '7' in str(i):
                cnt += 1
        print(cnt)
    except:
        break
