# 定义字母转数字和数字转字母（输出时要用）的字典

level = {
    'A': 1, 'J': 11, 'Q': 12, 'K': 13
}

reverse = {
    1: 'A', 11: 'J', 12: 'Q', 13: 'K'
}

# 递归，注意看题目要求，不用括号，并且顺序计算，那么当前值要放在后面
def cal(nums, val):
    if len(nums) == 1:
        if nums[0] != val:
            return None
        else:
            return str(nums[0]) if 2<=nums[0]<=9 else reverse[nums[0]]
    for i in range(len(nums)):
        rest = nums[:i] + nums[i+1:]
        res = cal(rest, val - nums[i])
        cur = str(nums[i]) if 2<=nums[i]<=9 else reverse[nums[i]]
        if res:
            return res + '+' + cur 
        res = cal(rest, val + nums[i])
        if res:
            return res + '-' + cur
        res = cal(rest, val / nums[i])
        if res:
            return res + '*' + cur
        res = cal(rest, val * nums[i])
        if res:
            return res + '/' + cur
    return None

while True:
    try:
        nums = input().split()
        if 'joker' in nums or 'JOKER' in nums:
            print('ERROR')
            continue
        for i in range(4):
            if nums[i] in level.keys():
                nums[i] = level[nums[i]]
            else:
                nums[i] = int(nums[i])
        res = cal(nums, 24)
        if not res: # 注意python中None和题目要求的不一样
            print('NONE')
        else:
            print(res)
    except:
        break
