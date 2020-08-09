# res记录当前可以称出的结果，每个结果都加上下一个可以称出的结果

while True:
    try:
        n = int(input())
        res = {0}
        weights = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        for i in range(n):
            for item in res.copy():
                res |= set(range(item, item+weights[i]*(nums[i]+1), weights[i]))
        print(len(res))
    except:
        break
