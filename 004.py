# 长度超过8循环输出，切片取后面的（复杂度高了点，不过切片比较快，8个8个一遍历会好点）；不到8位格式化输出
while True:
    try:
        s = input()
        while len(s)>8:
            print(s[:8])
            s = s[8:]
        print('{:0<8}'.format(s))
    except:
        break
