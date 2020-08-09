# 多分情况讨论一下就好了，注意可能不到4首歌的情况

def up(num, cur, window):
    if cur == window[0]:
        if window[0] != 0:
            window[0] -= 1
            window[1] -= 1
        else:
            window[1] = num-1
            window[0] = max(num-4, 0)
    return (cur - 1)%num
        
def down(num, cur, window):
    if cur == window[-1]:
        if window[-1] != num-1:
            window[0] += 1
            window[1] += 1
        else:
            window[0] = 0
            window[1] = min(num-1, 3)
    return (cur + 1)%num

while True:
    try:
        num = int(input())
        orders = input()
        window = [0, min(num-1, 3)]
        cur = 0
        for order in orders:
            if order == 'U':
                cur = up(num, cur, window)
            else:
                cur = down(num ,cur, window)
        print(' '.join(map(str, range(window[0]+1, window[1]+2))))
        print(cur+1)
    except:
        break
