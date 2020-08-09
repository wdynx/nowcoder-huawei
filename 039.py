# 判断ip是不是合法，和之前一样，这里好像不用管mask是不是1开头了，题目也没说
def islegal(ip):
    if ip.count('.') != 3:
        return False
    ip = list(filter(lambda x: x and 0<=int(x)<=255, ip.split('.')))
    return len(ip) == 4

while True:
    try:
        mask = input()
        ip1 = input()
        ip2 = input()
        if islegal(mask) and islegal(ip1) and islegal(ip2):
            mask = list(map(int, mask.split('.')))
            ip1 = list(map(int, ip1.split('.')))
            ip2 = list(map(int, ip2.split('.')))
            flag = 0
            # 一个一个或，有不一样就错
            for i in range(4):
                if ip1[i]|mask[i] != ip2[i]|mask[i]:
                    flag = 2
                    break
            print(flag)
        else:
            print(1)
    except:
        break
