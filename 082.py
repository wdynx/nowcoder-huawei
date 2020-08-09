# 这个题好像表述的不清楚 6/11 不能写成6个1/11么。。。
# 从1/2开始慢慢边小，比当前的数小就分离出来，否则接着找，知道原来的数的分子变成1
# math里面有最大公因数，自己写的话就辗转相除找

import math
while True:
    try:
        a, b = list(map(int, input().split('/')))
        GCD = math.gcd(a, b)
        a //= GCD
        b //= GCD
        base = 2
        res = []
        while a != 1:
            if a*base>=b:
                a *= base
                a -= b
                b *= base
                res.append(base)
                GCD = math.gcd(a, b)
                a //= GCD
                b //= GCD
            base += 1
        res.append(b)
        print('+'.join(map(lambda x: '1/'+str(x), res)))
    except:
        break
