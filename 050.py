# 先讲一个拒绝offer的小技巧

while True:
    try:
        print(eval(input()))
    except:
        break
        
# 用堆栈做了，注意可能出现负号，前面添一个0即可
level = {
    '+': 0, '-': 0,
    '*': 1, '/': 1
}
# 定义操作符
op_dic = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}

while True:
    try:
        express = input()
        ls = []
        for i in express:
            if i.isdigit() and ls and ls[-1].isdigit():
                ls[-1] += i # 数字放一起
            elif i in {'(', '[', '{'}:
                ls.append('(')
            elif i in {')', ']', '}'}:
                ls.append(')')
            elif i == '-' and (not ls or not ls[-1].isdigit() and not ls[-1] == ')'):
                ls.append('0')
                ls.append(i)
            else:
                ls.append(i)
        stack_num = []
        stack_op = []
        for i in ls:
            if i.isdigit():
                stack_num.append(int(i))
            else:
                if i == '(':
                    stack_op.append(i)
                elif i == ')':
                    while stack_op[-1] != '(':
                        op = stack_op.pop()
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        stack_num.append(op_dic[op](num1, num2))
                    stack_op.pop()
                else:
                    while stack_op and stack_op[-1] != '(' and level[stack_op[-1]] >= level[i]:
                        op = stack_op.pop()
                        num2 = stack_num.pop()
                        num1 = stack_num.pop()
                        stack_num.append(op_dic[op](num1, num2))
                    stack_op.append(i)
        while stack_op:
            op = stack_op.pop()
            num2 = stack_num.pop()
            num1 = stack_num.pop()
            stack_num.append(op_dic[op](num1, num2))
        print(stack_num[0])
    except:
        break
