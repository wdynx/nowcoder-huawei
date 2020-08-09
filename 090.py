while True:
    try:
        ip = input().split('.')
        ip = list(filter(lambda x: x and x.isdigit() and 0<=int(x)<256, ip))
        if len(ip) == 4:
            print('YES')
        else:
            print('NO')
    except:
        break
