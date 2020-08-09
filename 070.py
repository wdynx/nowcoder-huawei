# 堆栈做，注意有一个测试多一个反括号

def cal(x, y, z):
    return x*y*z

while True:
    try:
        n = int(input())
        matrix = []
        for i in range(n):
            matrix.append(list(map(int, input().split())))
        express = input()
        stack = []
        cur = 0
        res = 0
        for sym in express:
            if sym == '(':
                stack.append('(')
            elif sym == ')':
                if len(stack)<2:
                    continue
                nxt = stack.pop()
                stack.pop()
                if stack and stack[-1] != '(':
                    last = stack.pop()
                    res += cal(last[0], last[1], nxt[1])
                    stack.append((last[0], nxt[1]))
                else:
                    stack.append(nxt)
            else:
                nxt = matrix[cur]
                cur += 1
                if stack and stack[-1] != '(':
                    last = stack.pop()
                    res += cal(last[0], last[1], nxt[1])
                    stack.append((last[0], nxt[1]))
                else:
                    stack.append(nxt)
        print(res)
    except:
        break
