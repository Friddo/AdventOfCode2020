

l = []

for n in range(1,1001):
    a = input().split(" ")
    a[0] = a[0].split("-") # range
    a[1] = a[1][0] #special character
    l.append(a)
i = 0
for n in l:
    b = 0
    if n[2][int(n[0][0])-1] == n[1]:
        b+=1
    if n[2][int(n[0][1])-1] == n[1]:
        b+=1
    if b == 1:
        i+=1
    print(n[2][int(n[0][0])-1], n[2][int(n[0][1])-1], b)
print(i)
