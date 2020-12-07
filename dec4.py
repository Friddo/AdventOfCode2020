import re
l = ""
for n in range(1,990):
    l = l + input() + " "
l = [s.strip() for s in l.split('  ') if s]
l = [s.split(" ") for s in l]
total = 0
for n in l:
    if len(n) >= 7:
        o = 0
        a = [0]*7
        for i in n:
            t = i.split(":")
            ds = t[1]

            t = t[0]
            if t == "byr":
                if int(ds) >= 1920 and int(ds) <= 2002:
                    print(int(ds))
                    a[0]+=1
            elif t == "iyr":
                if int(ds) >= 2010 and int(ds) <= 2020:
                    a[1]+=1
            elif t == "eyr":
                if int(ds) >= 2020 and int(ds) <= 2030:
                    a[2]+=1
            elif t == "hgt":
                text = ds[-2] + ds[-1]
                if ds[0:-3] != "":
                    num = int(ds[0:-2])
                    print(text,num)
                    if text == "cm":
                        if num >= 150 and num <= 193:
                            a[3]+=1
                    if text == "in":
                        if num >= 59 and num <= 76:
                            a[3]+=1
            elif t == "hcl":
                match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', ds)
                if match:
                    a[4]+=1
            elif t == "ecl":
                match = re.search(r'amb|blu|brn|gry|grn|hzl|oth', ds)
                if match:
                    a[5]+=1
            elif t == "pid":
                if len(ds) == 9:
                    a[6]+=1
        print(a)
        for i in a:
            if i == 1:
                o+=1
        if o == 7:
            total+=1
print(total)