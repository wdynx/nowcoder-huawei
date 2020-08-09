# 二分法

while True:
    try:
        num = float(input())
        flag = 1
        if num < 0:
            num = -num
            flag = -1
        elif num == 0:
            print(0)
            continue
        left, right = 0, num+1
        while right - left > 0.01:
            mid = (left + right) / 2
            if mid**3 <= num:
                left = mid
            else:
                right = mid
        print(round(left, 1))
    except:
        break
