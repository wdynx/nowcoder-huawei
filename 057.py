# python可以直接处理长整型，好像内部还是当成字符串在做，所以有时间还是自己实现一下吧

while True:
    try:
        num1 = int(input())
        num2 = int(input())
        print(num1+num2)
    except:
        break
