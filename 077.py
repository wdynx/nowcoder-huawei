# 力扣面试题 08.09
# 进来看作push，出去看作pop
# 任何时候，pop数量不可能超过push
# 模拟一下所有情况，再排个序
# 推销一下力扣上自己的解题
# https://leetcode-cn.com/problems/bracket-lcci/solution/pai-lie-zu-he-wen-ti-by-becauseiambatman/

while True:
    try:
        n = int(input())
        ls = list(map(int, input().split()))
        seq = list(range(n))
        res = []
        while True:
            stack = []
            nums = ls.copy()
            seq_set = set(seq)
            operators = [0 if i in seq_set else 1 for i in range(2*n)]
            cur = []
            for operator in operators:
                if operator == 0:
                    stack.append(nums.pop(0))
                else:
                    cur.append(stack.pop())
            res.append(cur)
            if sum(seq) == n*(n-1):
                break
            for i in range(n-1, -1, -1):
                if seq[i] != 2*i:
                    seq[i] += 1
                    for j in range(i+1, n):
                        seq[j] = seq[j-1]+1
                    break
        for item in sorted(res):
            print(' '.join(map(str, item)))
    except:
        break
