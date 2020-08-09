while True:
    try:
        num = bin(int(input()))[2:] # bin后是0b开头，要去掉
        res = 0
        cur = 0
        for i in num:
            if i == '1':
                cur += 1
            else:
                if cur > res:
                    res = cur
                cur = 0
        if cur > res:
            res = cur
        print(res)
    except:
        break
