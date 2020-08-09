# 这个题就解方程了，当然直接算出来也行吧

while True:
    try:
        input()
        for i in range(200 // 14 + 1):
            if (200 - 14*i) % 8 == 0:
                j = (200 - 14*i) // 8
                k = 100 - i - j
                print(i, j, k)
    except:
        break
