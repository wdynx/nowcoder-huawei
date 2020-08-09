# 注意python中的len是看字符不是看字节，不能用

while True:
    try:
        s = input().split()
        s, n = s[0], int(s[1])
        cnt = 0
        res = []
        for i in s:
            if cnt == n:
                break
            if ord(i) < 128:
                cur = 1
            else:
                cur = 2
            if cnt + cur <= n:
                cnt += cur
                res.append(i)
            else:
                break
        print(''.join(res))
    except:
        break
