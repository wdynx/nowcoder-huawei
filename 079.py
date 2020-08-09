# 动态规划

while True:
    try:
        a = input()
        b = input()
        dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]
        for i in range(len(a)+1):
            for j in range(len(b)+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    dp[i][j] = min(dp[i-1][j-1]+(1 if a[i-1] != b[j-1] else 0), dp[i][j-1]+1, dp[i-1][j]+1)
        print('1/%d'%(dp[-1][-1]+1))
    except:
        break
