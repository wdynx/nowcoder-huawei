# 个人认为这是最难的一个题了
# 首先，考虑到除了2之外的质数都是奇数，那么相加的两数必定一奇一偶
# 而根据题目，是不可能加出2的
# 所以可以将输入的数据分成奇偶两类，类内不可能匹配，类间才能匹配
# 这就成了一个匹配问题，唯一的判定方式是两者之和是不是质数，必须一一检验
# 而这个配对是没有大小关系的，不能用贪心；新加入数字以后，可能配对方式完全不同，没有递推关系，也不能用动态规划
# 这样一个最大匹配问题了就只能用匈牙利算法了，具体原理网上有很多
# 简单说一下要注意的点，感觉很多解析都没提到
# 1.一轮只尝试匹配一个数
# 2.每个数在匹配的时候，从第一个能匹配的开始，能抢就抢，抢不了再看下一个
# 3.同一轮抢过了的要记录一下，不能反复抢，不然死循环了

# 用于返回所有可能的素数，题目要求30000以内，两个相加就是60000以内
def get_primes():
    primes = [2]
    for i in range(3, 60000):
        flag = 0
        for j in primes:
            if j > i**0.5: # 开方作为上限，省点时间
                break
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            primes.append(i)
    return primes

# 存循环外面吧，每次跑都一样，不影响
primes = set(get_primes())

# 匹配环节
# odd表示当前尝试匹配的奇数
# pairs是每个奇数可以匹配的所有偶数，字典形式，key=奇数，val=偶数集合
# matched是目前匹配上了的，字典形式，key=偶数，val=奇数，用来查找被抢的奇数是谁
# rest是这轮还没被抢过的所有偶数，集合形式，免得循环抢同一个造成死循环
def match(odd, pairs, matched, rest):
    for pair in pairs[odd]: # 对于每一个可以配对的偶数
        if pair in rest: # 如果可以抢
            rest.remove(pair) # 从可以抢的集合种剔除
            if pair not in matched.keys() or match(matched[pair], pairs, matched, rest): # 如果没匹配过，或者被抢的奇数可以腾出位置（尝试匹配被抢的奇数，此时rest中已经没有这个被抢的数了）
                matched[pair] = odd # 当前的奇数和这个可以抢的偶数配对
                return True # 配对成功
    return False # 所有可以配对的都配不了，匹配失败

while True:
    try:
        # 输入处理
        n = int(input())
        nums = list(map(int, input().split()))
        
        # 奇数偶数分类
        evens = []
        odds = []
        for num in nums:
            if num % 2 == 1:
                odds.append(num)
            else:
                evens.append(num)
                
        # 构建配对关系，记录每个奇数可以匹配的所有偶数，字典形式，key=奇数，val=偶数集合
        # 这里用二维列表应该也可以，字典省空间一点
        pairs = {}
        for i in odds:
            pairs[i] = set()
            for j in evens:
                if i + j in primes:
                    pairs[i].add(j)
        
        # 记录目前已经匹配上了的，字典形式，key=偶数，val=奇数，用来查找被抢的奇数是谁
        matched = {}
        for odd in odds:
            match(odd, pairs, matched, set(evens)) # 每一轮开始的时候，所有偶数都可以尝试抢
        print(len(matched)) # 输出有多少对即可
    except:
        break
