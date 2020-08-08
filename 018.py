# 情况比较多，慢慢写

# 判断是否非法
def islegal(ip, mask):
    
    # 先看是不是各有3个点
    if ip.count('.') != 3 or mask.count('.') != 3:
        return False
    
    # 拆成字符串列表，不能直接转int，可能会出错
    ip = ip.split('.')
    mask = mask.split('.')
    
    # 偷个懒，列表拼接一起判断
    # 先看是不是存在，可能有空字符
    # 再看是不是数字，可能有乱码
    # 再看范围对不对
    # 满足要求的刚好有8个就是对的
    if len(list(filter(lambda x: x and x.isdigit() and 0<=int(x)<256, ip+mask))) != 8:
        return False
        
    # 判断mask合不合法，转换2进制，注意开头的'0b'，以及补齐8位
    mask = ''.join(map(lambda x: '{:0>8}'.format(bin(int(x))[2:]), mask))
    # 直接数1有几个，全1全0的非法，不是连续1的非法
    n = mask.count('1')
    if n == 0 or n == 32:
        return False
    if mask != '1'*n + '0'*(32-n):
        return False
    return True

# 分类，直接if-else判断吧，返回的是下面ls列表中的索引
def classify(ip):
    ip = list(map(int, ip.split('.')))
    if ip[0] < 127:
        return 0
    elif ip[0] < 192:
        return 1
    elif ip[0] < 224:
        return 2
    elif ip[0] < 240:
        return 3
    else:
        return 4

# 判断是不是私有
def isprivate(ip):
    ip = list(map(int, ip.split('.')))
    if ip[0] == 10:
        return True
    if ip[0] == 172 and 16 <= ip[1] <32:
        return True
    if ip[0] == 192 and ip[1] == 168:
        return True
    return False

# 用于统计的列表，因为每个循环都要用，放在最前面
ls = [0, 0, 0, 0, 0, 0, 0]
while True:
    try:
        ip, mask = input().split('~')
        legal = islegal(ip, mask)
        if legal == False:
            ls[5] += 1
            continue
        if ip[0] == '0' or ip[:3] == '127':
            continue
        ls[classify(ip)] += 1
        if isprivate(ip):
            ls[6] += 1
    except:
        break
print(' '.join(map(str, ls)))
