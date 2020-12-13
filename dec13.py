from functools import reduce

time = int(input())
data = [int(x) if x.isdigit() else x for x in input().split(',')]


def p1(data):
    buses = [x for x in data if type(x) is int]
    res = [(x - time % x, x) for x in buses]
    return reduce(lambda x, y: x*y, min(res))

def p2(data):
    buses = [x for x in data if type(x) is int]
    mods = [-i%v for i, v in enumerate(data) if v!='x']
    x, step = 0, 1
    for d, r  in zip(buses, mods):
        while x % d != r:
            x += step
        step *= d
    return x


print(p1(data))
print(p2(data))