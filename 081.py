# 懒得自己计数了。。。用Counter吧

from collections import Counter
while True:
    try:
        flag = 0
        short = Counter(input())
        long = Counter(input())
        for key in short.keys():
            if key not in long.keys():
                print('false')
                flag = 1
                break
        if flag == 0:
            print('true')
    except:
        break
