
l = []
for n in range(0,594):
    l.append(input())


#format input
nestRules = {}
for n in l:
    b, a = n.strip('\n.').split('contain')
    outer = b.rstrip('bags ')
    inner = [b.strip("bags ").split(' ', 1) for b in a.split(',') if not 'no' in b]
    nestRules[outer] = inner


# part 1
def containShinyGold(bagColor):
    if 'shiny gold' in bagColor:
        return True
    else:
        return any(containShinyGold(color) for _, color in nestRules[bagColor])
#part 2
def numBagsContained(bagColor):
    if not nestRules[bagColor]:
        return 0
    else:
        return sum(int(num) + int(num) * numBagsContained(color) for num, color in nestRules[bagColor])


print(sum(containShinyGold(color) for color in nestRules.keys() if color != 'shiny gold'))
print(numBagsContained('shiny gold'))