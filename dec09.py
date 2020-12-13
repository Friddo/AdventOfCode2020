
l = []
for n in range(0,1000):
    l.append(int(input()))


def p1(codes, premable):
    previous_stack = []
    i = 0
    start = 0
    end = start+premable
    curr_index = premable
    while curr_index < len(codes)-1:
        stack = codes[start:end]
        if curr_index > len(stack)-1:
            start+=1
            end+=1
            valid = False
            for i in stack[:-1]:
                for j in stack[1:]:
                    #print(codes[curr_index], i, j)
                    if i+j == codes[curr_index]:
                        valid = True
                        break
                    else:
                        valid == False
                if valid:
                    break
            if valid == False:
                return codes[curr_index]

        curr_index+=1

inv = p1(l, 25)

import numpy as np

def p1(codes, invalid_num):
    contigous_list = []

    for i in range(0, len(codes)-1):
        for j in range(1, len(codes)-1):
            stack = np.array(codes[i:j])
            if np.sum(stack) == invalid_num:
                print(stack, stack.min()+stack.max())

p2(l, inv)

