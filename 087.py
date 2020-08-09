# 顺着写吧，没什么好说的

def length_score(s):
    if len(s)<=4:
        return 5
    elif len(s)<=7:
        return 10
    else:
        return 25
    
def alpha(s):
    ls = [i for i in s if i.isalpha()]
    if not ls:
        return 0
    else:
        s = ''.join(ls)
        if not s.isupper() and not s.islower():
            return 20
        else:
            return 10
        
def num(s):
    cnt = 0
    for i in s:
        if i.isdigit():
            cnt += 1
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 10
    else:
        return 20

def symbol(s):
    cnt = 0
    for i in s:
        if not i.isalnum():
            cnt += 1
    if cnt == 0:
        return 0
    elif cnt == 1:
        return 10
    else:
        return 25

while True:
    try:
        s = input()
        score = 0
        length = length_score(s)
        alp = alpha(s)
        digit = num(s)
        sym = symbol(s)
        if alp == 20 and digit >=10 and sym >= 10:
            score += 5
        elif alp == 10 and digit >= 10 and sym >= 10:
            score += 3
        elif alp >= 10 and digit >= 10:
            score += 2
        score += length + alp +digit + sym
        if score >= 90:
            print('VERY_SECURE')
        elif score >= 80:
            print('SECURE')
        elif score >= 70:
            print('VERY_STRONG')
        elif score >= 60:
            print('STRONG')
        elif score >= 50:
            print('AVERAGE')
        elif score >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break
