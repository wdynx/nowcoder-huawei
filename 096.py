while True:
    try:
        s = input()
        res = ''
        for i in s:
            if i.isalpha():
                if not res or res[-1].isalpha():
                    res += i
                else:
                    res += '*' + i
            else:
                if not res or res[-1].isalpha():
                    res += '*' + i
                else:
                    res += i
        if res and res[-1].isdigit():
            res += '*'
        print(res)
    except:
        break
