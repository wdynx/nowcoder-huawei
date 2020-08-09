# 闰年和2月判断一下

def isleap(x):
    return x % 4 == 0 and x % 100 != 0 or x % 400 == 0

dic = {
    1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151,
    7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334
}

month_day = {
    1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}

while True:
    try:
        year, month, day = list(map(int, input().split()))
        if year < 0 or month < 1 or month > 12 or day < 1 or day > month_day[month] or not isleap(year) and month == 2 and day == 29:
            print(-1)
        else:
            if isleap(year) and month > 2:
                print(dic[month] + 1 + day)
            else:
                print(dic[month] + day)
    except:
        break
