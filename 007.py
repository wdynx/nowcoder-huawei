# 拆分成整数和小数来处理，不要用round！不要用round！不要用round！
# In : round(0.5)
# Out: 0
while True:
    try:
        a, b = tuple(map(int, input().split('.')))
        if b >= 5:
            a += 1
        print(a)
    except:
        break
