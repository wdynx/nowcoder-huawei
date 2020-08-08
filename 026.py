# 不区分大小写，全小写以后排序，先比字典序，再比索引
# 其他的全部用字典记录索引位置，后面放进去

while True:
    try:
        s = input()
        dic = {}
        alpha_list = []
        for i in range(len(s)):
            if not s[i].isalpha():
                dic[i] = s[i]
            else:
                alpha_list.append((i, s[i]))
        alpha_list.sort(key=lambda x: (x[1].lower(), x[0]))
        res = []
        j = 0
        for i in range(len(s)):
            if i in dic.keys():
                res.append(dic[i])
            else:
                res.append(alpha_list[j][1])
                j += 1
        print(''.join(res))
    except:
        break
