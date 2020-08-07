# 直接sort，默认按照字典序排序
while True:
    try:
        n = int(input())
        ls = []
        for i in range(n):
            ls.append(input())
        ls.sort()
        for i in ls:
            print(i)
    except:
        break
