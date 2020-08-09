# 动态规划
# 只记录当前情况结尾的公共子串长度
# 建立dp的时候就可以顺带记录一下最优解
# 当然，后面再遍历一次是一样的，总是Omn

while True:
    try:
        s1 = input()
        s2 = input()
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
        best_i, best_j = 0, 0
        Max = 0
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i > 0 and j > 0 and s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j] > Max:
                        Max = dp[i][j]
                        best_i = i
                        best_j = j
        print(s1[best_i-Max:best_i])
    except:
        break
