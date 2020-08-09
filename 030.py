# 反正一共就16个数，变来变去太麻烦了，直接写好算了

dic = {
    '0': '0',
    '1': '8',
    '2': '4',
    '3': 'C',
    '4': '2',
    '5': 'A',
    '6': '6',
    '7': 'E',
    '8': '1',
    '9': '9',
    'a': '5',
    'b': 'D',
    'c': '3',
    'd': 'B',
    'e': '7',
    'f': 'F',
    'A': '5',
    'B': 'D',
    'C': '3',
    'D': 'B',
    'E': '7',
    'F': 'F',
}

# 按照要求先切片排序，后变形
# 英语不好，even和odd写反了，懒得改了，不要在意这些细节
def ProcessString(str1, str2):
    s = str1 + str2
    even = sorted(s[1::2])
    odd = sorted(s[::2])
    res = []
    for i in range(len(s)):
        div, mod = divmod(i, 2)
        if mod == 0:
            if odd[div] in dic.keys():
                res.append(dic[odd[div]])
            else:
                res.append(odd[div])
        else:
            if even[div] in dic.keys():
                res.append(dic[even[div]])
            else:
                res.append(even[div])
    return ''.join(res)

while True:
    try:
        str1, str2 = input().split()
        res = ProcessString(str1, str2)
        if res:
            print(res)
    except:
        break
