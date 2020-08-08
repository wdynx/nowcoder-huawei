# 这个类其实不写也一样，反正函数也只用一次
# 每个词都放在它的字典序最小单词里面
# 找的时候也先排序

class Dictionary:
    def __init__(self, num, words):
        self.num = num
        self.dic = self.process(words) # 排序后：单词列表
        
    def process(self,words):
        dic = {}
        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in dic.keys():
                dic[sorted_word] = []
            dic[sorted_word].append(word)
        return dic
    
    def get_brother(self, word):
        return self.dic.get(''.join(sorted(word)), [])
    
    def clear(self):
        self.num = 0
        self.dic = None
        
while True:
    try:
        s = input().split()
        num = int(s[0])
        words = s[1:1+num]
        target = s[-2]
        seq = int(s[-1]) - 1
        dic = Dictionary(num, words)
        brothers = dic.get_brother(target)
        brothers = sorted(list(filter(lambda x: x != target, brothers))) # 过滤掉自己以后排序
        print(len(brothers))
        if seq < len(brothers):
            print(brothers[seq])
    except:
        break
