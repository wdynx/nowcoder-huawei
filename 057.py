# python可以直接处理长整型，好像内部还是当成字符串在做，所以有时间还是自己实现一下吧

while True:
    try:
        num1 = int(input())
        num2 = int(input())
        print(num1+num2)
    except:
        break

# 常规做法
while True:
    try:
        a = input().strip()
        b = input().strip()
        if len(a) < len(b):
            a, b = b, a
        a = [i for i in a]
        b = [i for i in b]
        flag = 0
        res = []
        for i in range(len(a)):
            num = flag + int(a[-1-i]) + (int(b[-1-i]) if i < len(b) else 0)
            flag, num = divmod(num, 10)
            res.append(str(num))
        if flag == 1:
            res.append('1')
        print(''.join(res[::-1]))
    except:
        break
