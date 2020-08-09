# 斐波那契数列，用根号5的那个通项公式涉及到浮点计算，不一定可以

def getTotalCount(n):
    if n == 1 or n == 2:
        return 1
    else:
        return getTotalCount(n-1) + getTotalCount(n-2)
while True:
    try:
        n = int(input())
        print(getTotalCount(n))
    except:
        break
