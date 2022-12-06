def part_1():
    f = open("input.txt")
    line = f.readline()


    for i in range(4,len(line)):
        set = {line[i-4], line[i-3], line[i-2], line[i-1]}
        if len(set) == 4:
            return i

def part_2():
    f = open("input.txt")
    line = f.readline()
    for i in range(14,len(line)):
        s = set()
        for n in range(1,15):
            print(n)
            s.add(line[i-n])
        if len(s) == 14:
            return i
    
print(part_1())
print(part_2())