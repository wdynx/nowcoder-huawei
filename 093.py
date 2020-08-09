# 动态规划，求和等于sum/2

while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        Sum = sum(nums)
        if Sum % 2 == 1:
            print('false')
            continue
        target = Sum // 2
        ls = []
        for num in nums:
            if num%3 != 0 and num%5 != 0:
                ls.append(num)
            elif num%5 == 0:
                target -= num
        lim = sum(map(abs, ls))
        if abs(target) > lim:
            print('false')
            continue
        dp = [[False]*(2*lim+1) for _ in range(len(ls))]
        for i in range(len(ls)):
            for j in range(2*lim+1):
                if j == lim:
                    dp[i][j] = True
                elif i == 0:
                    if j == lim + ls[i]:
                        dp[i][j] = True
                else:
                    if dp[i-1][j]:
                        dp[i][j] = True
                    elif 0<=j-ls[i]<=2*lim and dp[i-1][j-ls[i]]:
                        dp[i][j] = True
        if dp[-1][target+lim]:
            print('true')
        else:
            print('false')
    except:
        break
