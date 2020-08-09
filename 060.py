# 先把前n个数中的质数找出来放着
# 遍历所有可能拆分，看是不是都是素数

while True:
    try:
        n = int(input())
        primes = [2]
        for i in range(3, n):
            isprime = 1
            for j in primes:
                if j > i**0.5:
                    break
                if i%j == 0:
                    isprime = 0
                    break
            if isprime:
                primes.append(i)
        primes_set = set(primes)
        for i in range(n//2, 1, -1):
            if i in primes_set and n-i in primes_set:
                print(i)
                print(n-i)
                break
    except:
        break
