import timeit

l = []
for n in range(0,901):
    l.append(input())
start = timeit.default_timer()
ids = []
missing = 0
for n in range(7,909):
    missing+=n
for n in l:
    r = 0
    for i in range(0,len(n)-3):
        if n[i] == "B":
            r += 2**(6-i)
    s = 0
    for i in range(0,3):
        if n[i+7] == "R":
            s += 2**(2-i)
    ids.append(r * 8 + s)
    missing-=r * 8 + s
print(min(ids), max(ids))
print(missing)
stop = timeit.default_timer()
print('Time: ', stop - start)




