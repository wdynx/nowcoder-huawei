# 动态规划
# 注意不区分大小写

while True:
    try:
        p = input().lower()
        q = input().lower()
        dp = [[0]*(len(q)+1) for _ in range(len(p)+1)]
        res = 0
        for i in range(len(p)+1):
            for j in range(len(q)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    if p[i-1] == q[j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                        if dp[i][j] > res:
                            res = dp[i][j]
                    else:
                        dp[i][j] = 0
        print(res)
    except:
        break
