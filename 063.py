# 滑窗

while True:
    try:
        dna = input()
        n = int(input())
        best = 0
        res = dna[:n].count('C')+dna[:n].count('G')
        cur = res
        for i in range(1, len(dna)-n):
            cur += int(dna[i-1+n] in {'C', 'G'})
            cur -= int(dna[i-1] in {'C', 'G'})
            if cur > res:
                res = cur
                best = i
        print(dna[best:best+n])
    except:
        break
