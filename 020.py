def islegal(psd):
    # 长度超过8
    if len(psd) <= 8:
        return 'NG'
        
    # 种类超过3
    kind = {'upper', 'lower', 'digit', 'else'}
    for i in psd:
        if i.isdigit():
            kind -= {'digit'}
        elif i.isupper():
            kind -= {'upper'}
        elif i.islower():
            kind -= {'lower'}
        else:
            kind -= {'else'}
    if len(kind) >= 2:
        return 'NG'
    
    # 相同长度大于2的子串重复 等同于相同长度为3的子串重复 重复4个也会重复3个嘛
    sub = set()
    for i in range(len(psd)-3):
        if psd[i:i+3] not in sub:
            sub.add(psd[i:i+3])
        else:
            return 'NG'
    return 'OK'
    
    
while True:
    try:
        psd = input()
        print(islegal(psd))
    except:
        break
