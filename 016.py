# 动态规划，背包问题
# 把附件全部放到主件上，这样每个主件有5种方案：不买，只买主，主+附1，主+附2，主+附1+附2
# dp记录只考虑前i个物品，花了j元（实际上是j*10）的最大收益是多少

while True:
    try:
        # 处理输入
        N, m = tuple(map(int, input().split()))
        info = [] # 记录物品信息
        dic = {} # 记录主附件信息，key = info中的编号，value二维列表形式记录，每行记录钱数和收益，第一个是主件，最多3行
        for i in range(m):
            info.append(list(map(int, input().split())))
            
        # 先记录主件，再添加附件，因为可能附件所属的主键还没添加进去，会报错
        # 题目说了都是10的倍数，和钱相关的都除以10，省空间，
        for i in range(len(info)):
            if info[i][2] == 0:
                dic[i] = [[info[i][0]//10, info[i][1]*info[i][0]]] # [价格//10，收益]
        for i in range(len(info)):
            if info[i][2] != 0:
                dic[info[i][2]-1].append([info[i][0]//10, info[i][1]*info[i][0]])
                
        # 修改一下，记录方式，变成最开始说的5种组合方案，注意加入不买的情况
        for k, v in dic.items():
            if len(v) == 1:
                dic[k] = [[0, 0],
                          [v[0][0], v[0][1]]]
            elif len(v) == 2:
                dic[k] = [[0, 0],
                          [v[0][0], v[0][1]], 
                          [v[0][0]+v[1][0], v[0][1]+v[1][1]]]
            else:
                dic[k] = [[0, 0],
                          [v[0][0], v[0][1]], 
                          [v[0][0]+v[1][0], v[0][1]+v[1][1]], 
                          [v[0][0]+v[2][0], v[0][1]+v[2][1]], 
                          [v[0][0]+v[1][0]+v[2][0], v[0][1]+v[1][1]+v[2][1]]]
        # 只取记录的值，key是info中的编号，用不上
        values = list(dic.values())
        
        # 创建dp，注意N也要除以10， 而且物品数量是主件数量，不是m
        dp = [[0]*(N//10+1) for _ in range(len(values))]
        
        # 动态规划，写入dp表，其实value可以再排序优化一下的，不过反正一共就5个，每一个可买的情况都比较一下，影响不大
        for i in range(len(values)):
            for j in range(N//10+1):
                for item in values[i]:
                    if i == 0:
                        if j >= item[0]:
                            dp[i][j] = max(dp[i][j], item[1])
                    else:
                        if j >= item[0]:
                            dp[i][j] = max(dp[i][j], item[1]+dp[i-1][j-item[0]])
        
        # 完事
        print(dp[-1][-1])
    except:
        break
