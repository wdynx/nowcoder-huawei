# bfs，然后再反着找回去

while True:
    try:
        m, n = list(map(int, input().split()))
        matrix = []
        for i in range(m):
            line = list(map(lambda x: -int(x), input().split()))
            matrix.append(line)
        cur = {(0, 0)}
        rnd = 1
        while matrix[-1][-1] == 0:
            nxt = set()
            for node in cur:
                matrix[node[0]][node[1]] = rnd
                if node[0] + 1 < m and matrix[node[0]+1][node[1]] == 0:
                    nxt.add((node[0]+1, node[1]))
                if node[1] + 1 < n and matrix[node[0]][node[1]+1] == 0:
                    nxt.add((node[0], node[1]+1))
            rnd += 1
            cur = nxt
        path = [(m-1, n-1)]
        node = (m-1, n-1)
        for i in range(m+n-2):
            if node[0]-1>=0 and matrix[node[0]-1][node[1]] == matrix[node[0]][node[1]] - 1:
                node = (node[0]-1, node[1])
            else:
                node = (node[0], node[1]-1)
            path.append(node)
        path.reverse()
        for node in path:
            print('({},{})'.format(node[0], node[1]))
    except:
        break
