while True:
    try:
        height = int(input())
        total = height * 3 - height / 8
        last = height / 32
        print(total)
        print(last)
    except:
        break
