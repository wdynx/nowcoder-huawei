# 经典动态规划

while True:
    try:
        s1 = input()
        s2 = input()
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = max(i, j)
                else:
                    if s1[i-1] == s2[j-1]:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
                    else:
                        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
        print(dp[-1][-1])
    except:
        break
