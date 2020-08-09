while True:
    try:
        # 输入直接转列表，方便map
        s = [i for i in input()]
        # 只要不是字母，统统换成空格
        s = ''.join(list(map(lambda x: x if x == ' ' or x.isalpha() else ' ', s)))
        # 倒序合并
        print(' '.join(reversed(s.split())))
    except:
        break
