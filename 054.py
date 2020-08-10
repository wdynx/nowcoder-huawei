# 和50题一样的，有时间还是别用eval

while True:
    try:
        print(eval(input()))
    except:
        break

# 定义优先级
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
