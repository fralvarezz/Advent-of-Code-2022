f = open("input.txt")

lines = f.readlines()
matrix = []

for i in range(len(lines)):
    lines[i] = lines[i].replace("\n","")
    matrix.append([False]*len(lines[i]))

def find_result():
    count = 0
    for row in matrix:
        for el in row:
            if el == True:
                count += 1
    print(count)

#populate matrix
for row in range(len(lines)):
    for column in range(len(lines[0])):
        if row == 0 or column == 0 or row == len(lines)-1 or column == len(lines[0])-1:
            matrix[row][column] = True

#first rows, then columns
for row in range(len(lines)):
    highest = 0

    for column in range(len(lines[row])):
        number = int(lines[row][column])
        if matrix[row][column] == True:
            highest = max(highest, number)
            continue
        
        if number > highest:
            highest = number
            matrix[row][column] = True
    
    highest = 0
    for column in range(len(lines[row])-1, 0, -1):
        number = int(lines[row][column])
        if matrix[row][column] == True:
            highest = max(highest, number)
            continue
        
        if number > highest:
            highest = number
            matrix[row][column] = True

#first columns, then rows
for column in range(len(lines[0])):
    highest = 0

    for row in range(len(lines)-1):
        number = int(lines[row][column])
        if matrix[row][column] == True:
            highest = max(highest, number)
            continue
        
        if number > highest:
            highest = number
            matrix[row][column] = True

    highest = 0
    for row in range(len(lines)-1, 0, -1):
        number = int(lines[row][column])
        if matrix[row][column] == True:
            highest = max(highest, number)
            continue
        
        if number > highest:
            highest = number
            matrix[row][column] = True


find_result()

#part 2
distances_matrix = [[1]*99 for i in range(99)]

#first rows, then columns
for row in range(len(lines)):
    distances_in_current = [0]*10
    for column in range(len(lines[row])):
        number = int(lines[row][column])
        closest = 0

        for height in range(number, 10):
            closest = max(closest, distances_in_current[height])
        distances_in_current[number] = column
        distances_matrix[row][column] *= (column - closest)
          
    distances_in_current = [len(lines[row])-1]*10
    for column in range(len(lines[row])-1, 0, -1):
        number = int(lines[row][column])
        closest = len(lines[row])-1
        for height in range(number, 10):
            closest = min(closest, distances_in_current[height])
        distances_in_current[number] = column
        distances_matrix[row][column] *= (closest - column)

#first columns, then rows
for column in range(len(lines[0])):
    distances_in_current = [0]*10

    for row in range(len(lines)-1):
        number = int(lines[row][column])
        closest = 0
        for height in range(number, 10):
            closest = max(closest, distances_in_current[height])
        distances_in_current[number] = row
        distances_matrix[row][column] *= (row - closest)


    distances_in_current = [len(lines[row])-1]*10
    for row in range(len(lines)-1, 0, -1):
        number = int(lines[row][column])
        closest = len(lines[row])-1
        for height in range(number, 10):
            closest = min(closest, distances_in_current[height])
        distances_in_current[number] = row
        distances_matrix[row][column] *= (closest - row)


max_found = 0
for row in distances_matrix:
    for el in row:
        max_found = max(max_found, int(el))
print(max_found)


