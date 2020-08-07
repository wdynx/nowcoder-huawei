# bin函数转二进制字符，转换后开头两位是'0b'，不影响数'1'的个数
while True:
    try:
        num = int(input())
        print(bin(num).count('1'))
    except:
        break
