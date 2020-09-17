def floor_sum(n, m, a, b):
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)

    y_max = (a * n + b) // m
    x_max = y_max * m - b
    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans


def check_floor_sum():
    T = int(input())
    for _ in range(T):
        n, m, a, b = [int(_) for _ in input().split()]
        print(floor_sum(n, m, a, b))

if __name__ == '__main__':
    # https://judge.yosupo.jp/problem/sum_of_floor_of_linear
    check_floor_sum()
