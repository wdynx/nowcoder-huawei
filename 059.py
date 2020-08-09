# 先数一遍，顺着找第一个

while True:
    try:
        s = input()
        char = {}
        for i in s:
            char[i] = char.get(i, 0) + 1
        flag = 0
        for i in s:
            if char [i] == 1:
                print(i)
                flag = 1
                break
        if flag == 0:
            print(-1)
    except:
        break
