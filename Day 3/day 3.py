def part_1():
    f = open("input.txt")
    total = 0
    for el in f:
        compartment1 = el[:int(len(el)/2)]
        compartment2 = el[int(len(el)/2):]

        matching = [x for x in compartment1 if x in compartment2][0]
        
        priority = ord(matching.lower()) - ord('a') + 1
        if matching.isupper():
            priority = priority + 26

        total = total + priority
    print(total)

def part_2():
    f = open("input.txt")
    total = 0
    lines = f.readlines()
    for i in range(0,len(lines),3):
        matching = [x for x in lines[i] if x in lines[i+1] and x in lines[i+2]][0]
        
        priority = ord(matching.lower()) - ord('a') + 1
        if matching.isupper():
            priority = priority + 26

        total = total + priority
    print(total)

part_1()
part_2()