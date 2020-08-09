# 顺着数

while True:
    try:
        dic = {
            'alpha': 0,
            'space': 0,
            'digit': 0,
            'other': 0
        }
        s = input()
        for i in s:
            if i.isalpha():
                dic['alpha'] += 1
            elif i == ' ':
                dic['space'] += 1
            elif i.isdigit():
                dic['digit'] += 1
            else:
                dic['other'] += 1
        print(dic['alpha'])
        print(dic['space'])
        print(dic['digit'])
        print(dic['other'])
    except:
        break
