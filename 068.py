# 多个排序条件用元组，这个时候不要用reverse参数，会同时reverse的

while True:
    try:
        n = int(input())
        reverse = input() == '0'
        ls = []
        for i in range(n):
            ls.append(input().split())
            ls[-1].append(i)
        ls.sort(key=lambda x: (-int(x[1]) if reverse else int(x[1]), x[2]))
        for item in ls:
            print(item[0], item[1])
    except:
        break
