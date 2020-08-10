# 和前面32一样的，不过这次有个输入用力是空，要额外判断一下

def manacher(password):
    max_right = -1
    center = -1
    radius = []
    res = 0
    for i in range(len(password)):
        mirror = center * 2 - i
        if i < max_right and i + radius[mirror] < center + radius[center]:
            radius.append(radius[mirror])
        else:
            for j in range(max(0, max_right-i), 1 + min(i, len(password)-i-1)):
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
        inputs = input()
        if not inputs:
            break
        password = '#' + '#'.join(list(inputs)) + '#'
        res = manacher(password)
        print(res)
    except:
        break
