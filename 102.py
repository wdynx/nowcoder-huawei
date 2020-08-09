# 多排序规则用元组操作
# 用例好像不涉及非ascii码的情况

from collections import Counter
while True:
    try:
        s = Counter(input())
        res = sorted(list(s.keys()), key=lambda x:(-s[x], ord(x)))
        print(''.join(map(str, res)))
    except:
        break
