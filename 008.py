# 字典get方法
while True:
    try:
        dic = {}
        n = int(input())
        for i in range(n):
            key, val = list(map(int, input().split()))
            dic[key] = dic.get(key, 0) + val
        for item in dic.items():
            print(item[0], item[1])
    except:
        break
