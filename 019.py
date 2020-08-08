# 个人感觉这个题描述的不是很清楚
# 最后出现的8条记录在前面有重复的时候，是刷新还是不刷新？（实际上是不刷新，只记录新出现的，另一种会更难写）

# 记录全部出错文件及其位置
ls = []
# 记录个数
dic = {}
while True:
    try:
        msg = input().split()
        # 路径\分割，只取最后一个
        msg[0] = msg[0].split('\\')[-1]
        # 取后16位，再字符串形式拼回去（元组应该也可以）
        msg = ' '.join([msg[0][-16:], msg[1]])
        # 不再字典中就记录一下
        if msg not in dic.keys():
            ls.append(msg)
            dic[msg] = 1
        # 在字典中就只计数
        else:
            dic[msg] += 1
    except:
        break
# 只要后8位
for item in ls[-8:]:
    print(item, dic[item])
