while True:
    try:
        a = input()
        b = input()
        if len(a) < len(b):
            a, b = b, a
        a = [i for i in a]
        b = [i for i in b]
        flag = 0
        res = []
        for i in range(len(a)):
            num = flag + int(a[-1-i]) + (int(b[-1-i]) if i < len(b) else 0)
            flag, num = divmod(num, 10)
            res.append(str(num))
        if flag == 1:
            res.append('1')
        print(''.join(res[::-1]))
    except:
        break
