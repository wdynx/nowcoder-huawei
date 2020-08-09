# 最好的做法是写个前缀树出来
# 不过这个题情况不多，暴力点不用动脑筋

dic = {
    'reset': 'reset what',
    'reset board': 'board fault',
    'board add': 'where to add',
    'board delete': 'no board at all',
    'reboot backplane': 'impossible',
    'backplane abort': 'install first',
    'else': 'unknown command'
}

while True:
    try:
        order = input().split()
        if len(order) == 1:
            if 'reset'.startswith(order[0]):
                print(dic['reset'])
            elif 'reboot'.startswith(order[0]):
                print(dic['reboot backplane'])
            elif 'backplane'.startswith(order[0]) and order[0] != 'b':
                print(dic['backplane abort'])
            else:
                print(dic['else'])
        else:
            if 'reset'.startswith(order[0]) and 'board'.startswith(order[1]) and 'reboot'.startswith(order[0]) and 'backplane'.startswith(order[1]):
                print(dic['else'])
            elif 'reset'.startswith(order[0]) and 'board'.startswith(order[1]):
                print(dic['reset board'])
            elif 'reboot'.startswith(order[0]) and 'backplane'.startswith(order[1]):
                print(dic['reboot backplane'])
            elif 'board'.startswith(order[0]) and 'delete'.startswith(order[1]):
                print(dic['board delete'])
            elif 'board'.startswith(order[0]) and 'add'.startswith(order[1]) and 'backplane'.startswith(order[0]) and 'abort'.startswith(order[1]):
                print(dic['else'])
            elif 'board'.startswith(order[0]) and 'add'.startswith(order[1]):
                print(dic['board add'])
            elif 'backplane'.startswith(order[0]) and 'abort'.startswith(order[1]):
                print(dic['backplane abort'])
            else:
                print(dic['else'])
    except:
        break
