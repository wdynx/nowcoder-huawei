while True:
    try:
        s = input()
        cnt = 0
        for i in s:
            if i.isupper():
                cnt += 1
        print(cnt)
    except:
        break
