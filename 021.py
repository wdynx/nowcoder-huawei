# 先写个表，对着转换就行了，z单独拿出来写吧，专门写个%26太麻烦

dic = {'a': 2, 'b': 2, 'c': 2,
       'd': 3, 'e': 3, 'f': 3, 
       'g': 4, 'h': 4, 'i': 4, 
       'j': 5, 'k': 5, 'l': 5, 
       'm': 6, 'n': 6, 'o': 6, 
       'p': 7, 'q': 7, 'r': 7, 's': 7, 
       't': 8, 'u': 8, 'v': 8, 
       'w': 9, 'x': 9, 'y': 9, 'z': 9}
while True:
    try:
        psd = input()
        res = ''
        for i in psd:
            if i.isdigit():
                res += i
            elif i.isupper():
                if i == 'Z':
                    res += 'a'
                else:
                    res += chr(1 + ord(i.lower()))
            else:
                res += str(dic[i])
        print(res)
    except:
        break
