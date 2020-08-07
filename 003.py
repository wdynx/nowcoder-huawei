# set去重，sort排序
while True:
    try:
        n = int(input())
        array = []
        for i in range(n):
            array.append(int(input()))
        array = list(set(array))
        array.sort()
        for num in array:
            print(num)
    except:
        break
