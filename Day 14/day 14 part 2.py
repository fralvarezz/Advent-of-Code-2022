import bisect

f = open("input")
columns = []
highest = 0
for el in f:
    li = el.replace("\n","").split(" -> ")

    for i in range(len(li)-1):
        left = [int(x) for x in li[i].split(",")]
        right = [int(x) for x in li[i+1].split(",")]
        

        while (len(columns)) <= left[0]:
            columns.append([])
        
        while (len(columns)) <= right[0]:
            columns.append([])
        highest = max(max(highest, left[1]), max(highest, right[1]))
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

for i in range(len(columns)):
    bisect.insort(columns[i],highest+2)

for i in range(20):
    columns.append([highest+2])

#print(columns)
pos = (500,0)
stop = False
count = 0
while not stop:
    count+=1
    pos = (500,0)
    put = False
    while not put:
        #print("Not put: ",pos)
        #print(columns[pos[0]])
        for occupied in columns[pos[0]]:
            #found a place
            if pos[1] < occupied:
                if len(columns) - 1 == pos[0]:
                    columns.append([highest+2])
                    columns.append([highest+2])  
                #down left
                #pos = (pos[0],occupied-1)

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
            if pos == (500,0):
                stop = True
                put = True
                count-=1
                break


print(count)
    #bisect.insort(columns[starting[0]],starting[1])

    #pos = columns[starting[0]].index(starting[1])


    

