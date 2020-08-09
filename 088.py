# 每个牌给个点数好比较
level = {
    '3': 1, '4': 2, '5': 3, '6': 4,
    '7': 5, '8': 6, '9': 7, '10': 8,
    'J': 9, 'Q': 10, 'K': 11, 'A': 12,
    '2': 13, 'joker': 14, 'JOKER': 15
}

# 判断是不是炸弹，不是就取0
def isBomb(s):
    if set(s) == {'joker', 'JOKER'}:
        return 14
    if len(s) == 4 and len(set(s)) == 1:
        return level[s[0]]
    else:
        return 0

# 长度代表类型，最小的点数用来比较
def judge(s):
    return len(s), min(list(map(lambda x: level[x], s)))

while True:
    try:
        left, right = tuple(input().split('-'))
        left = left.split()
        right = right.split()
        bomb_left = isBomb(left) 
        bomb_right = isBomb(right)
        if bomb_left != 0 or bomb_right != 0:
            if bomb_left > bomb_right:
                print(' '.join(left))
            else:
                print(' '.join(right))
        else:
            type_left, value_left = judge(left)
            type_right, value_right = judge(right)
            if type_left != type_right:
                print('ERROR')
            else:
                if value_left > value_right:
                    print(' '.join(left))
                else:
                    print(' '.join(right))
    except:
        break
