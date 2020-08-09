# 转2进制数一下即可
# 也可以循环移位

while True:
    try:
        print(bin(int(input())).count('1'))
    except:
        break
