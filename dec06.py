l,i = "", 0
for n in range(0,2172):
    l+=input()+" "
l = [a.split(" ") for a in l.split("  ")]
l[-1].pop() #hotfix
for n in l:
    t = set(n[0])
    for a in range(0,len(n)):
        t = t.intersection(n[a])
    i+=len(t)
print(i)

