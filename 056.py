# 其实完备数没多少，不怕被喷可以面向答案编程
# 这里遍历检查每个数
# 不要把所有的因子都找出来，会超时
# 和检查质数一样，只到根号i即可

while True:
    try:
        n = int(input())
        cnt = 0
        for i in range(2, n+1):
            cur = 1
            for j in range(2, 1+int(i**0.5)):
                if i%j == 0:
                    cur += j+i//j if i != j else 0
            if cur == i:
                cnt += 1
        print(cnt)
    except:
        break
