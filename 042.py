# 考英语的

numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
    20, 30, 40, 50, 60, 70, 80, 90, 
]
english = [
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
    'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
    'eighty', 'ninety'
]
dic = dict(zip(numbers, english))
while True:
    try:
        num = input()
        if len(num) > 9 or not num.isdigit():
            print('error')
            continue
        num = int(num)
        res = []
        groups = ['million', 'thousand', None]
        while num:
            group = groups.pop()
            if group:
                res.append(group)
            num, mod = divmod(num, 1000)
            digit1, digit2, digit3 = mod//100, mod//10%10, mod%10
            if digit2 == 1:
                res.append(dic[mod%100])
            else:
                if digit3 in dic.keys():
                    res.append(dic[digit3])
                if digit2 in dic.keys():
                    res.append(dic[digit2*10])
            if digit1 != 0:
                res.append('and')
                res.append('hundred')
                res.append(dic[digit1])
        res.reverse()
        print(' '.join(res))
    except:
        break
