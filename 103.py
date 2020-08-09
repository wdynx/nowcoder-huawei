# 最长上升子序列
# 动态规划On2
# 贪心+二分Onlogn （24题）
# 树状数组不会

while True:
    try:
        n = int(input())
        ls = list(map(int, input().split()))
        dp = [1]*len(ls)
        for i in range(1, len(ls)):
            for j in range(i):
                if ls[j] < ls[i]:
                   dp[i] = max(dp[i], dp[j]+1)
        print(max(dp))
    except:
        break
