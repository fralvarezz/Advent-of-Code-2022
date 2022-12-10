f = open("input.txt")

head = (0,0)
tail = (0,0)

movements = {
    "U": (0,1),
    "D": (0,-1),
    "R": (1,0),
    "L": (-1,0)
}

touched = set()
last_dir = (0,0)


def distance(pos1, pos2):
    dist = (abs(pos2[0] - pos1[0]), abs(pos2[1] - pos1[1]))
    return max(dist[0], dist[1])


def find_closest(tail, from_position, to_position):
    if distance(tail, to_position) <= 1:
        return tail

    direc = (to_position[0]-tail[0], to_position[1]-tail[1]) 

    if direc[0] > 1:
        direc = (1, direc[1])

    if direc[1] > 1:
        direc = (direc[0], 1)

    if direc[0] < -1:
        direc = (-1, direc[1])

    if direc[1] < -1:
        direc = (direc[0], -1)

    return (tail[0] + direc[0], tail[1] + direc[1]) 

def move(from_position, direction):
    return (from_position[0] + direction[0], from_position[1] + direction[1])

touched.add((0,0))
parts = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

for line in f:
    direction = movements[line[0]]
    times = int(line[2:-1])

    for i in range(times):
        from_pos = (0,0)
        to_pos = (0,0)
        direction = movements[line[0]]

        for j in range(len(parts)):
            
            if j == 0:
                from_pos = parts[j]
                to_pos = move(parts[j], direction)
                parts[j] = to_pos
            else:
                if distance(parts[j], parts[j-1]) > 1:
                    go_to = find_closest(parts[j], from_pos, to_pos)
                    prev = parts[j]
                    parts[j] = go_to
                    from_pos = prev
                    to_pos = go_to
                    #print("Direction",direction)
            
                    

            if j == 9:
                touched.add(parts[j])


            
        #if i == times-1:
        print(line[0],": ",i)
        for part in parts:
            print(part)
        print("-----------------------")

print(len(touched))
    