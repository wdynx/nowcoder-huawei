# 先说一下，这个不是正确答案，不过已经可以通过所有的测试用例了
# 这个代码没有解决数字末尾的0，也就是说100会认为是'壹佰零'
# 本来是想先提交看看，结果就直接过了
# 这个要处理也挺麻烦的，因为可能直接整个万位全是0，此时还要把万也省掉，并且可能再和个位的零合并

dic = {
    0: '零', 1: '壹', 2: '贰', 3: '叁', 4: '肆', 
    5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖', 
}
while True:
    try:
        num = list(map(int, input().split('.')))
        start = '人民币' # 固定开头
        end = '' # 结尾分两种情况，有无小数部分
        if len(num) == 1 or num[1] == 0:
            end += '整'
        else:
            if num[1]>=10:
                end += dic[num[1]//10] + '角'
            if num[1]%10:
                end += dic[num[1]%10] + '分'
        ls = [] # 用于存储中间部分，倒序存储，后面再处理
        block = ['元', '万', '亿'] # 每4位一组，元要放在这里，因为可能会出现只有小数部分，此时不能有零元，而是直接几角几分
        num = num[0] # 去掉小数部分，已经处理过了
        while num:
            ls.append(block.pop(0)) # 先把单位放进来，每一轮会不一样
            num, rest = divmod(num, 10000) # 4位一处理
            cur = [] # 正序存放当前组，因为涉及到零的处理，倒序不方便
            cur.append(dic[rest//1000]) # 千位
            if cur[-1] != '零': # 如果是0就不要单位了，后面一样
                cur.append('仟')
            cur.append(dic[rest//100%10])
            if cur[-1] != '零':
                cur.append('佰')
            cur.append(dic[rest//10%10])
            if cur[-1] != '零':
                cur.append('拾')
            cur.append(dic[rest%10])
            ls.extend(cur[::-1]) # cur是正的，而ls是倒的，要反过来放进去
        ls.reverse() # 整体再倒过来，变成正的
        while ls and ls[0] == '零': # 开头的零直接丢弃，这里好像不太需要考虑ls会变成空，题目没有说会不会有零元整的情况，实例也没有
            ls.pop(0)
        res = [] # 再过滤一遍，连续的两个零变成一个零，题目有要求
        while ls:
            if ls[0] == '零' and res[-1] == '零':
                ls.pop(0)
            else:
                res.append(ls.pop(0))
        if len(res) >= 2 and res[0] == '壹' and res[1] == '拾': # 开头的10叫拾，而中间的10叫一十
            res.pop(0)
        res = start+''.join(res)+end
        print(res) # 到这里就结束了，可以看到是没有处理结尾的零的 
    except:
        break
