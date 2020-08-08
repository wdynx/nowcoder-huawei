# 最长子序列问题，左右各一次，然后找加起来最多的
# 偷个懒用bisect，因为要求小于，相同情况取最左边

import bisect
while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        left, right = [], []
        store = []
        for num in nums:
            idx = bisect.bisect_left(store, num)
            if idx == len(store):
                store.append(num)
            else:
                store[idx] = num
            left.append(idx)
        store = []
        for num in nums[::-1]:
            idx = bisect.bisect_left(store, num)
            if idx == len(store):
                store.append(num)
            else:
                store[idx] = num
            right.append(idx)
        right.reverse()
        res = 0
        for i in range(len(nums)):
            if left[i]+right[i] > res:
                res = left[i] + right[i]
        print(len(nums) - res - 1)
        
    except:
        break
