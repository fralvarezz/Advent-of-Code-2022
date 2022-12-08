from collections import deque

def create_path(optional=None, stop_at=None):
    path = ""
    i = 0
    for d in dir_queue:
        path += d
        if d != "/":
            path += "/"

        if stop_at == i:
            break
        else:
            i+=1
    if optional is not None:
        path += optional
        path += "/"

    if(path[:-1] == ""):
        return "/"
    else:
        return path[:-1]


f = open("input.txt")
lines = f.readlines()

dir_queue = deque()

explored_dirs = []
exploring = False
dirs = {}
dir_sizes = {"/": 0}

for i in range(len(lines)):
    line = lines[i]
    line = line[:-1]

    if "$ cd " in line:
        exploring = False
        next_dir = line.replace("$ cd ", "")
        if next_dir == "..":
            dir_queue.pop()
        else:
            dir_queue.append(next_dir)

    elif "$ ls" in line:
        if create_path() not in explored_dirs:
            exploring = True
            explored_dirs.append(create_path())
            
    else:
        if not exploring:
            continue

        file_info = line.split(" ")
        #if create_path() not in dirs:
        #    dirs[create_path()] = []

        if "dir" in file_info[0]:
        #    dirs[create_path()].append(("dir", file_info[1]))
            if file_info[1] not in dir_sizes:
                dir_sizes[create_path(file_info[1], None)] = 0
        else:
            
            #dirs[create_path()].append((file_info[1], int(file_info[0])))
            print("Adding at: " + create_path())
            for i in range(len(dir_queue)):
                dir_sizes[create_path(None, i)] += int(file_info[0])
                print(create_path(None, i))
            

cnt = 0
for k,v in dir_sizes.items():
    if v <= 100000:
        #print(k,v)
        cnt+=v
print("part 1: " + str(cnt))

smallest = 70000000
used_size = dir_sizes["/"]
remaining_size = 70000000-used_size

for k,v in dir_sizes.items():
    if v + remaining_size > 30000000:
        smallest = min(smallest, v)

print("part 2: " + str(smallest))



    