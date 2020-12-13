

l = []
for n in range(1,201):
    l.append(int(input()))

for a in l:
    for b in l:
        if a + b == 2020:
            print(a+b)
            break

for a in l:
    for b in l:
        for c in l:
            if a + b + c == 2020:
                print(a*b*c)
                break