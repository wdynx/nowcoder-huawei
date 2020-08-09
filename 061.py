# 动态规划

while True:
    try:
        m, n = list(map(int, input().split()))
        # m=0单独处理一下
        if m == 0:
            print(1)
            continue
        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 只有一个苹果或者只有一个盘子的情况
                if i == 0 or j == 0: 
                    dp[i][j] = 1
                # 这个递推很关键，因为交换次序是一样的，不如就让苹果数量是降序的
                # 也就是说最后一个篮子里只能有0到(i+1)//(j+1)个
                else:
                    for k in range((i+1)//(j+1)+1):
                        dp[i][j] += dp[i-k*(j+1)][j-1] if i >= k*(j+1) else 1 # 这里要判断一下，可能刚好不剩苹果，但是我们的假设是从1个苹果开始的
        print(dp[-1][-1])
    except:
        break
