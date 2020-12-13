l = []

for n in range(0,596):
    l.append(input().split())
# Part 1

def calcAcc(l):
    visited = set()
    acc = i = 0
    while i not in visited:
        visited.add(i)
        if i >= len(l):
            return acc, True
        instruction, value = l[i]
        if instruction == 'nop':
            i += 1
        elif instruction == 'jmp':
            i += int(value)
        else:
            i += 1
            acc += int(value)
    return acc, False


print(calcAcc(l)[0])

# Part 2

for i, item in enumerate(l):
    instruction, value = item
    if instruction == "acc":
        continue
    if instruction == "nop":
        l[i] = ("jmp", value)
        acc, terminated = calcAcc(l)
    else:
        l[i] = ("nop", value)
        acc, terminated = calcAcc(l)
    l[i] = [instruction, value]
    if terminated:
        print(acc)
        break

