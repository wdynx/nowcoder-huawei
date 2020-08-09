# 按题目要求的接口写的，其实duck不必
# 数字直接对10取余，就可以实现循环
# 字母当然也可以对26取余，不过ord chr的太麻烦，直接分情况讨论了

def Encrypt(aucPassword, aucResult):
    ls = []
    for i in aucPassword:
        if i.isdigit():
            ls.append(str((int(i)+1)%10))
        elif i.isupper():
            if i == 'Z':
                ls.append('a')
            else:
                ls.append(chr(ord(i)+1).lower())
        elif i.islower():
            if i == 'z':
                ls.append('A')
            else:
                ls.append(chr(ord(i)+1).upper())
    aucResult[0] = ''.join(ls)

def unEncrypt(result, password):
    ls = []
    for i in result:
        if i.isdigit():
            ls.append(str((int(i)+9)%10))
        elif i.isupper():
            if i == 'A':
                ls.append('z')
            else:
                ls.append(chr(ord(i)-1).lower())
        elif i.islower():
            if i == 'a':
                ls.append('Z')
            else:
                ls.append(chr(ord(i)-1).upper())
    password[0] = ''.join(ls)
    
while True:
    try:
        aucPassword = input()
        result = input()
        # 这里看题目要求没有返回值，就用列表传进去修改了，其实可以就直接返回，不用这么麻烦
        aucResult = [None]
        password = [None]
        Encrypt(aucPassword, aucResult)
        unEncrypt(result, password)
        print(aucResult[0])
        print(password[0])
    except:
        break
