# 经典最小堆，保留k个，全塞一遍
# 不考虑空间问题也可以快排

import heapq
while True:
    try:
        n, k = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        ls = []
        heapq.heapify(ls)
        # 这里这样写其实不太好，最好还是只保留k个，现场pop掉
        # 因为这种问题要解决的就是数太多空间太少
        for num in nums:
            heapq.heappush(ls, num)
        res = []
        for i in range(k):
            res.append(heapq.heappop(ls))
        print(' '.join(map(str, res)))
    except:
        break
