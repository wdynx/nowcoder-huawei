# 马拉车算法，利用回文字符串性质
# 也可以暴力中心扩散，不过On2可能会超时

def manacher(password):
    max_right = -1
    center = -1
    radius = []
    res = 0
    for i in range(len(password)):
        mirror = center * 2 - i
        if i < max_right and i + radius[mirror] < center + radius[center]: # 没越界
            radius.append(radius[mirror])
        else:
            for j in range(max(0, max_right-i), 1 + min(i, len(password)-i-1)): # 可能越界，从右边界开始中心扩散
                if password[i+j] == password[i-j]:
                    max_right = i+j
                    center = i
                    r = j
                else:
                    break
            radius.append(r)
        if radius[-1] > res:
            res = radius[-1]
    return res

while True:
    try:
        password = '#' + '#'.join(list(input())) + '#' # 插入'#'变奇数，方便处理
        res = manacher(password) # 处理后回文半径和处理前字符串长度相同
        print(res)
    except:
        break
