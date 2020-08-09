while True:
    try:
        s = input()
        idx = []
        longest = 0
        cur = 0
        for i in range(len(s)):
            if s[i].isdigit():
                cur += 1
                if cur > longest:
                    idx = [i]
                    longest = cur
                elif cur == longest:
                    idx.append(i)
            else:
                cur = 0
        res = list(map(lambda x:s[x-longest+1: x+1], idx))
        print(''.join(res), end='')
        print(','+str(longest))
    except:
        break
