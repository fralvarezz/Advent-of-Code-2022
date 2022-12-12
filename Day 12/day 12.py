import string
import math
import queue

class Node:
    height = 0
    neighbours = []
    dist = 100000
    previous = []
    is_goal = False
    pos = (0,0)

    def __init__(self, h):
        self.height = h
        self.previous = []
        self.neighbours = []
        self.dist = 100000
        self.is_goal = False
        self.pos = (0,0)

    def __lt__(self, __o):
        return self.dist < __o.dist
    
    def __eq__(self, __o) -> bool:
        return self.dist == __o.dist

    def __str__(self) -> str:
        return "Node at:" + str(self.pos) + " and distance " + str(self.dist)

    def reset(self):
        self.previous = [] 

f = open("input.txt")
lines = f.readlines()
cnt = len(lines) * (len(lines[0])-1)
maze = []
visited = []
m = 100000


f = open("input.txt")
lines = f.readlines()
cnt = len(lines) * (len(lines[0])-1)
maze = []
prio = queue.PriorityQueue()
candidates = []

picked = False
#initialize queue and maze
for i in range(len(lines)):
    maze.append([])
    for j in range(len(lines[i])):
        el = lines[i][j]
        node = Node(0)
        if el == "\n":
            continue
        elif el == "E":
            height = string.ascii_lowercase.find("z")
            node.height = height
            node.is_goal = True
        elif el == "S":
            node.height = 0
        else:
            height = string.ascii_lowercase.find(el)
            node.height = height
        node.pos = (i,j)
            
        if node.height == 0:
            candidates.append(node.pos)

        prio.put(node)
        maze[i].append(node)
        
#add neighbours
indices = [-1, 1]
for i in range(len(maze)):
    for j in range(len(maze[i])):
        for idx in indices:
            if i+idx >= 0 and i+idx < len(maze):
                neighbour = maze[i+idx][j]
                neighbour_height = neighbour.height
                if neighbour_height - maze[i][j].height <= 1:
                    maze[i][j].neighbours.append(neighbour)

            if j+idx >= 0 and j+idx < len(maze[i]):
                neighbour = maze[i][j+idx]
                neighbour_height = neighbour.height
                if neighbour_height - maze[i][j].height <= 1:
                    maze[i][j].neighbours.append(neighbour)

#dijkstra
while not prio.empty():
    node = prio.get_nowait()
    for neigh in node.neighbours:
        distan = node.dist + 1
        if distan < neigh.dist:
            neigh.dist = distan
            neigh.previous = node
            prio.put(neigh)

m = 100000

for cand in candidates:
    print(cand)

while len(candidates) > 0:
    picked = False
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            node = maze[i][j]
            if node.height == 0 and (node.pos) in candidates and not picked:
                candidates.remove(node.pos)
                #print(node.pos)
                #print(len(candidates))
                node.dist = 0
                picked = True
            else:
                node.dist = 100000
            node.reset()
            prio.put(node)
    
    while not prio.empty():
        node = prio.get_nowait()
        for neigh in node.neighbours:
            distan = node.dist + 1
            if distan < neigh.dist:
                neigh.dist = distan
                neigh.previous = node
                prio.put(neigh)

    for li in maze:
        for no in li:
            if no.is_goal:
                m = min(m, no.dist)

print(m)