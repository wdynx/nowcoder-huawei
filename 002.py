# 全部转小写，顺着数一遍
while True:
    try:
        s = input().lower()
        target = input().lower() # 这里可以不转，测试用例都是小写
        cnt = 0
        for i in s:
            if i == target:
                cnt += 1
        print(cnt)
    except:
        break
