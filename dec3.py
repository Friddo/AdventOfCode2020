


l = []

for n in range(1,324):
    l.append(input())


sl = len(l[0])

v = 2
h = 1

pos = [0,0]
t = 1
for n in range(1,324):
    if pos[0] > len(l)-1:
        break
    if l[pos[0]][pos[1]] == "#":
        t +=1
        print("Hit at: ", end="")
        print(pos)

    pos = [pos[0]+v,(pos[1]+h) % sl]
print(t-1)