# 遇到引号判断一下

while True:
    try:
        cmds = input().split()
        res = []
        flag = 0
        for cmd in cmds:
            if flag == 0:
                if cmd.startswith('"'):
                    flag = 1
                res.append(cmd)
            else:
                if cmd.endswith('"'):
                    flag = 0
                res[-1] += cmd
        print(len(res))
        for cmd in res:
            print(cmd)
    except:
        break
