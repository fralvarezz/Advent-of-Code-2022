import bisect

f = open("input")
columns = []
for el in f:
    li = el.replace("\n","").split(" -> ")

    for i in range(len(li)-1):
        left = [int(x) for x in li[i].split(",")]
        right = [int(x) for x in li[i+1].split(",")]
        

        while (len(columns)) <= left[0]:
            columns.append([])
        
        while (len(columns)) <= right[0]:
            columns.append([])

        if left[0] == right[0]:
            if right[1] > left[1]:
                numbers = list(range(left[1], right[1]+1))
            else:
                numbers = list(range(left[1], right[1]-1, -1))
            
            for num in numbers:
                if num not in columns[left[0]]:
                    bisect.insort(columns[left[0]],(num))

        else:
            if right[0] > left[0]:
                numbers = list(range(left[0], right[0]+1))
            else:
                numbers = list(range(left[0], right[0]-1, -1))
            for num in numbers:
                if left[1] not in columns[num]:
                    bisect.insort(columns[num],(left[1]))
        
#print(columns)
pos = (500,0)
stop = False
count = 0
while len(columns[pos[0]]) > 0:
    print(pos)
    print(max(columns[pos[0]]), pos[1])
    count+=1
    pos = (500,0)
    put = False
    while not put:
        if len(columns[pos[0]]) == 0:
            count-=1
            break
        #print(pos)
        for occupied in columns[pos[0]]:
            #found a place
            if pos[1] < occupied:
                #down left
                if occupied not in columns[pos[0]-1]:
                    pos = (pos[0]-1, occupied)
                    break
                #down right
                elif occupied not in columns[pos[0]+1]:
                    pos = (pos[0]+1, occupied)
                    break
                else:
                    pos = (pos[0], occupied-1)
                    bisect.insort(columns[pos[0]],occupied-1)
                    put = True
                    break
print(count)
    #bisect.insort(columns[starting[0]],starting[1])

    #pos = columns[starting[0]].index(starting[1])


    

