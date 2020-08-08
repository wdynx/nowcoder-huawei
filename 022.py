# 有两瓶直接借了喝掉还，相当于每两个空瓶白嫖一瓶，直接除以2

while True:
    try:
        num = int(input())
        if num == 0:
            continue
        print(num // 2)
    except:
        break
