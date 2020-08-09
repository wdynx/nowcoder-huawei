# 这个题好像前面有的样子

while True:
    try:
        n = int(input())
        for i in range(n):
            s = input()
            if s == '':
                continue
            while len(s) > 8:
                print(s[:8])
                s = s[8:]
            print(s + '0'*(8-len(s)))
    except:
        break
