# 从2开始循环分解，不用担心i变到合数，能整除合数必定能整除合数的因数，所以遇到合数必不能整除
while True:
    try:
        num = int(input())
        factor = []
        i = 2
        while i <= num:
            while num % i == 0:
                num //= i
                factor.append(i)
            i += 1
        for i in factor:
            print(str(i) + ' ', end='')
        print()
    except:
        break
