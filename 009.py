# set记录一下出现过哪些，重复的不再添加
while True:
    try:
        s = input()
        ls = []
        ls_set = set()
        for i in s[::-1]:
            if i not in ls_set:
                ls_set.add(i)
                ls.append(i)
        print(''.join(ls))
    except:
        break
