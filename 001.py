# 按空格分割以后取最后一个字符串即可
while True:
    try:
        s = input().split()[-1]
        print(len(s))
    except:
        break
