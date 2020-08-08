# 计数找最小就好了，from collections import Counter更方便

while True:
    try:
        dic = {}
        s = input()
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        cnt, alpha_set = len(s), set()
        for item in dic.items():
            if item[1] == cnt:
                alpha_set.add(item[0])
            elif item[1] < cnt:
                cnt = item[1]
                alpha_set = set(item[0])
        res = ''
        for i in s:
            if i not in alpha_set:
                res += i
        print(res)
    except:
        break
