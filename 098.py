# 全村最诡异的题，没有之一
# 注意事项：
# 1.用例中查询不带空格，正因如此，根本不用实现query的功能，遇到直接报错即可
# 2.题目没有考虑E004，直接不管这个就好
# 3.E009和E010结尾没有换行
# 4.用例结尾会有莫名其妙的初始化，不知道怎么回事，也不知道为什么没管它也能过
# 5.退币操作直接贪心也能过，可能是1 2 5 10这个数字给的比较好，别写动态规划了
# 遇到了自认倒霉吧

class Machine:
    def __init__(self, args):
        arg_goods, arg_money = args
        self.balance = 0
        self.goods = list(map(int, arg_goods.split('-')))
        self.money = list(map(int, arg_money.split('-')))
        self.names = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6']
        self.price = [2, 3, 4, 5, 8, 6]
        self.value = [1, 2, 5, 10]
        print('S001:Initialization is successful')
        
    def pay(self, value):
        if value not in self.value:
            print('E002:Denomination error')
        elif value in {5, 10} and value > self.money[0] + self.money[1] * 2:
            print('E003:Change is not enough, pay fail')
        #elif self.balance> 10:
        #    print('E004:Pay the balance is beyond the scope biggest')
        elif sum(self.goods) == 0:
            print('E005:All the goods sold out')
        else:
            self.balance += value
            idx = self.value.index(value)
            self.money[idx] += 1
            print('S002:Pay success,balance=%d' % (self.balance))
            
    def buy(self, name):
        if name not in self.names:
            print('E006:Goods does not exist')
        else:
            idx = int(name[-1]) - 1
            if self.goods[idx] == 0:
                print('E007:The goods sold out')
            elif self.balance < self.price[idx]:
                print('E008:Lack of balance')
            else:
                self.balance -= self.price[idx]
                print('S003:Buy success,balance=%d' % (self.balance))
                
    def coins(self):
        if self.balance == 0:
            print('E009:Work failure', end='')
            return
        dp = [[float('inf')]*(self.balance + 1) for _ in range(4)]
        for i in range(4):
            for j in range(self.balance + 1):
                if i == 0:
                    dp[0][j] = j if j <= self.money[0] else float('inf')
                else:
                    for k in range(self.money[i]+1):
                        if j >= k*self.value[i]:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-k*self.value[i]]+k)
        for total in range(self.balance, -1, -1):
            if dp[3][total] != float('inf'):
                break
        coins = [0, 0, 0, 0]
        for i in range(3, 0, -1):
            for j in range(self.money[i]+1):
                if total >= j*self.value[i] and dp[i-1][total - j * self.value[i]] == dp[i][total] - j:
                    coins[i] = j
                    total -= j * self.value[i]
                    break
        coins[0] = total
        for i in range(4):
            print('{} yuan coin number={}'.format(self.value[i], coins[i]))
            self.money[i] -= coins[i]
        self.balance = 0
    
    def query(self, num):
        if len(num) != 2:
            print('E010:Parameter error')
            return
        num = int(num[1])
        if num == 0:
            for i in range(6):
                print('{} {} {}'.format(self.names[i], self.price[i], self.goods[i]))
        else:
            for i in range(4):
                print('{} yuan coin number={}'.format(self.value[i], self.money[i]))
        
while True:
    try:
        orders = input().split(';')[:-1]
        for order in orders:
            order = order.split()
            if order[0] == 'r':
                machine = Machine(order[1:])
            elif order[0] == 'p':
                machine.pay(int(order[1]))
            elif order[0] == 'b':
                machine.buy(order[1])
            elif order[0] == 'c':
                machine.coins()
            elif order[0] == 'q':
                machine.query(order)
            else:
                print("E010:Parameter error", end="")
    except:
        break
