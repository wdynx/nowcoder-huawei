# 考虑所有数字顺序，计算顺序，符号种类
# 懒得剪枝了

from itertools import permutations, combinations, product
functions = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x / y if y != 0 else float('inf')
]

cal_seq = list(permutations(range(3), 3))
syms = list(product(range(4), range(4), range(4)))

while True:
    try:
        nums = list(map(int, input().split()))
        nums_seq = list(permutations(nums, 4))
        flag = 0
        for ls in nums_seq:
            for seq in cal_seq:
                for sym in syms:
                    res = []
                    used = [0, 0, 0, 0]
                    for i in seq:
                        if used[i] == 0 and used[i+1] == 0:
                            res.append(functions[sym[i]](ls[i], ls[i+1]))
                            used[i] = 1
                            used[i+1] = 1
                        elif used[i] == 1 and used[i+1] == 1:
                            res.append(functions[sym[i]](res[0], res[1]))
                        elif used[i] == 1:
                            res.append(functions[sym[i]](res[-1], ls[i+1]))
                            used[i+1] = 1
                        else:
                            res.append(functions[sym[i]](ls[i], res[-1]))
                            used[i] = 1
                    if res[-1] == 24:
                        print('true')
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
        if flag == 0:
            print('false')
    except:
        break
