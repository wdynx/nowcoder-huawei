# 加密函数
def encrypt(key, data):
    key = key.upper() # 全转大写
    key_set = set(key) # 去重
    new_key = [] # 按顺序保留一个
    for i in key:
        if i in key_set:
            key_set.remove(i)
            new_key.append(i)
    alpha = [chr(i) for i in range(ord('A'), ord('Z')+1)] # 生成字母表
    new_key.extend(list(filter(lambda x: x not in new_key, alpha))) # 添加上没有的
    table = dict(zip([chr(i) for i in range(ord('A'), ord('Z')+1)], new_key)) # 打包成字典
    res = []
    # 一一对应输出
    for i in data:
        if i.isupper():
            res.append(table[i])
        else:
            res.append(table[i.upper()].lower())
    return ''.join(res)
    
while True:
    try:
        key = input()
        data = input()
        print(encrypt(key, data))
    except:
        break
