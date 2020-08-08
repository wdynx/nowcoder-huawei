# 分号分割指令，过滤掉无效的
# 定义4个移动的函数，也可以if-else

func = {
    'A': lambda loc, x: (loc[0]-x, loc[1]),
    'W': lambda loc, x: (loc[0], loc[1]+x),
    'S': lambda loc, x: (loc[0], loc[1]-x),
    'D': lambda loc, x: (loc[0]+x, loc[1]),
}
while True:
    try:
        orders = list(filter(lambda x: 2<=len(x)<=3 and x[0] in func.keys() and x[1:].isdigit(), input().split(';')))
        loc = (0, 0)
        for order in orders:
            loc = func[order[0]](loc, int(order[1:]))
        print(str(loc[0])+','+str(loc[1]))
    except:
        break
