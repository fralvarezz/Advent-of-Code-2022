def part_1():
    f = open("input.txt")
    total = 0
    for el in f:
        elves = el.split(",")
        rooms = []
        for elve in elves:
            rooms.append(elve.split("-"))
        
        if (int(rooms[0][0]) <= int(rooms[1][0]) and int(rooms[0][1]) >= int(rooms[1][1])) or (int(rooms[1][0]) <= int(rooms[0][0]) and int(rooms[1][1]) >= int(rooms[0][1])):
            total = total + 1
    print(total)

def part_2():
    f = open("input.txt")
    total = 0
    for el in f:
        elves = el.split(",")
        rooms = []
        for elve in elves:
            rooms.append(elve.split("-"))
        
        rooms1 = range(int(rooms[0][0]),int(rooms[0][1])+1)
        rooms2 = range(int(rooms[1][0]),int(rooms[1][1])+1)
        if any(x in rooms1 for x in rooms2):
            total = total + 1
    print(total)

part_1()
part_2()