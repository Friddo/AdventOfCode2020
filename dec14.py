import re

l = []
for n in range(0,562):
    l.append(input().strip())

#part 1
mask = None
memory = {}

for i in l:
    if i.startswith('mem'):
        addr, value = re.findall('mem\[(\d+)\] = (\d+)', i)[0]
        masked_value = ''.join([
            v if m == 'X' else m for m, v in zip(mask, format(int(value), '036b'))
        ])
        memory[addr] = ''.join(masked_value)
    else:
        mask = re.findall('mask = ([10X]{36})', i)[0]

print(sum([int(value, 2) for _, value in memory.items()]))


#part 2
mask = None
memory = {}

for i in l:
    if i.startswith('mem'):
        addr, value = re.findall('mem\[(\d+)\] = (\d+)', i)[0]

        masked_addr = ''.join([
            'X' if m == 'X' else '1' if m == '1' else v for m, v in zip(mask, format(int(addr), '036b'))
        ])

        all_addreses = [masked_addr]
        for i in range(masked_addr.count('X')):
            new_addreses = []
            for addr in all_addreses:
                next_X = next(i for i, c in enumerate(addr) if c == 'X')
                new_addreses.append(addr[:next_X] + '1' + addr[next_X+1:])
                new_addreses.append(addr[:next_X] + '0' + addr[next_X+1:])
            all_addreses = new_addreses

        for addr in all_addreses:
            memory[addr] = format(int(value), '036b')
    else:
        mask = re.findall('mask = ([10X]{36})', i)[0]

print(sum([int(value, 2) for _, value in memory.items()]))