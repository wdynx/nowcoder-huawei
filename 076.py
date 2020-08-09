# n**3 = n*n**2 就是一个长度是n的等差数列，均值是n2

while True:
    try:
        n = int(input())
        start = n**2 - n + 1
        ls = range(start, start+2*n, 2)
        print('+'.join(map(str, ls)))
    except:
        break
