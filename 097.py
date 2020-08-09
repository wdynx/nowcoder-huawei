while True:
    try:
        pos = 0
        pos_cnt = 0
        neg_cnt = 0
        n = int(input())
        nums = list(map(int, input().split()))
        neg_cnt = len(list(filter(lambda x: x<0, nums)))
        pos_cnt = len(list(filter(lambda x: x>0, nums)))
        pos = sum(list(filter(lambda x: x>0, nums)))
        print(neg_cnt, round(pos/pos_cnt, 1))
    except:
        break
