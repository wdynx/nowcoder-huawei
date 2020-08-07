# int直接转10进制了；写个字典一一对应，移位相加也可
while True:
    try:
        hex_num = input()
        print(int(hex_num, 16))
    except:
        break 
