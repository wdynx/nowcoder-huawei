# 把ip看成256进制数即可

while True:
    try:
        ip = list(map(int, input().split('.')))
        res = 0
        for i in range(4):
            res *= 256
            res += ip[i]
        print(res)
        ip = int(input())
        res = []
        while ip != 0:
            res.append(str(ip%256))
            ip //= 256
        while len(res) < 4:
            res.append('0')
        res.reverse()
        print('.'.join(res))
    except:
        break
