# 动态规划，递推情况比较多
# 最好还是别用re

while True:
    try:
        p = input()
        q = input()
        dp = [[True]*(len(q)+1) for _ in range(1+len(p))]
        for i in range(len(p)+1):
            for j in range(len(q)+1):
                if i == j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = False
                elif j == 0:
                    if dp[i-1][j] == True and p[i-1] == '*':
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if dp[i-1][j-1] == True and p[i-1] in {'?', '*', q[i-1]}:
                        dp[i][j] = True
                    elif dp[i-1][j] == True and p[i-1] == '*':
                        dp[i][j] = True
                    elif dp[i][j-1] == True and p[i-1] == '*':
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
        if dp[-1][-1]:
            print('true')
        else:
            print('false')
    except:
        break
