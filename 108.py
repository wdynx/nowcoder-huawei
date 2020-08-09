# 专门说了求最小公倍数，还是实现一遍辗转相除吧
import math
while True:
    try:
        a, b = map(int, input().split())
        gcd = math.gcd(a, b)
        print(a * b // gcd)
    except:
        break
        
# 辗转相除
def get_gcd(a, b):
    while a%b != 0:
        a, b = b, a%b
    return b
    
while True:
    try:
        a, b = map(int, input().split())
        gcd = get_gcd(a, b)
        print(a * b // gcd)
    except:
        break
