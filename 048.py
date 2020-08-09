# 列表代替链表了

while True:
    try:
        info = list(map(int, input().split()))
        num = info.pop(0)
        ls = [info.pop(0)]
        for i in range(num-1):
            nxt, lst = info.pop(0), info.pop(0)
            idx = ls.index(lst)
            ls.insert(idx+1, nxt)
        delete = info.pop()
        ls.remove(delete)
        print(' '.join(map(str, ls))+' ')
    except:
        break
