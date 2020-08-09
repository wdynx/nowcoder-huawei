# 按照出现次数排序，多的权重大

while True:
    try:
        n = int(input())
        for i in range(n):
            name = input()
            dic = {}
            for j in name:
                dic[j] = dic.get(j, 0) + 1
            weights = sorted(dic.items(), key=lambda x: x[1], reverse=True)
            res = 0
            for i in range(len(weights)):
                res += (26-i)*weights[i][1]
            print(res)
    except:
        break
