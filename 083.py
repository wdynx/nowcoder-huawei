# 测试用例要交换的两个格子在一行
# 题目说是可以插入0到m，其实是0到m-1
# 插入后也不能超过9

while True:
    try:
        row, col = tuple(map(int, input().split()))
        if row <= 9 and col <= 9:
            print(0)
        else:
            print(-1)
        row1, col1, row2, col2= tuple(map(int, input().split()))
        if 0<=row1<row and 0<=row2<row and 0<=col1<col and 0<=col2<col:
            print(0)
        else:
            print(-1)
        row_ins = int(input())
        if 0<=row_ins<row and row != 9:
            print(0)
        else:
            print(-1)
        col_ins = int(input())
        if 0<=col_ins<col and col != 9:
            print(0)
        else:
            print(-1)
        row3, col3 = tuple(map(int, input().split()))
        if 0<=row3<row and 0<=col3<col:
            print(0)
        else:
            print(-1)
    except:
        break
