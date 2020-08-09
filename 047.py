# 这个题讲的不是很清楚
# 如果后面值更小，那么认为是一个新序列，要重新开始处理
# 插值可能出现除不尽的情况，先计算梯度并取整，再按梯度插值

while True:
    try:
        m = list(map(int, input().split()))[0]
        syn = []
        for i in range(m):
            syn.append(list(map(int, input().split())))
        res = []
        for item in syn:
            if not res or res[-1][0]>item[0]:
                res.append(item)
            elif res[-1][0] == item[0]:
                continue
            else:
                grad = int((item[1] - res[-1][1]) / (item[0] - res[-1][0]))
                for i in range(res[-1][0]+1, item[0]):
                    res.append([i,res[-1][1]+grad])
                res.append([item[0], item[1]])
        for item in res:
            print(item[0], item[1])
    except:
        break
