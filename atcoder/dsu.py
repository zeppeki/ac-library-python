class dsu:
    def __init__(self, N):
        self.root = [-1 for _ in range(N)]
        self.size = [1 for _ in range(N)]

    def merge(self, x, y):
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            self.root[x] = y
            self.size[y] += self.size[x]
        else:
            self.root[y] = x
            self.size[x] += self.size[y]
    
    def leader(self, x):
        while self.root[x] >= 0:
            x = self.root[x]
        return x

    def same(self, x, y):
        return self.leader(x) == self.leader(y)


if __name__ == '__main__':
    ## https://judge.yosupo.jp/problem/unionfind
    
    N, Q = [int(_) for _ in input().split()]
    uf = dsu(N)

    for i in range(Q):
        t, u, v = [int(_) for _ in input().split()]
        if t == 0:
            uf.merge(u, v)
        else:
            if uf.same(u, v):
                print(1)
            else:
                print(0)
