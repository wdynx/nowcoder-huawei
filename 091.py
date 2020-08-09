# m次往又，n次往下
# C(m)(m+n)
# 这里不让用scipy.special，就用combinations代替了
# 求阶乘直接算也行
# 常规做法是排列组合，不过这样会快一些

from itertools import combinations
while True:
    try:
        m, n = list(map(int, input().split()))
        print(len(list(combinations(range(m+n), m))))
    except:
        break
