def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right: return -1
        if left > right: return +1
        return 0

    else:
        left = list([left]) if isinstance(left, int) else left
        right = list([right]) if isinstance(right, int) else right

        if len(left) == 0 and len(right) != 0: return -1
        if len(right) == 0 and len(left) != 0: return 1
        if len(left) == 0 and len(right) == 0: return 0
    
    ret = compare(left[0], right[0])
    if ret != 0:
        return ret
    else:
        return compare(left[1:], right[1:])

def get_list_from_input(_input):
    #print("Received ", _input)
    li = []
    brackets = []
    left = 0
    right = 0
    first_left = 100000
    last_right = 0
    i = 0
    while i < len(_input):
        if _input[i] == "[":
            brackets.append((i,"["))
            first_left = min(first_left, i)
            left += 1
        elif _input[i] == "]":
            right += 1
            last_right = max(last_right, i)
            if left == right:
                el = brackets.pop()
                li.append(get_list_from_input(_input[first_left+1:last_right]))
                left = 0
                right = 0
                first_left = 100000
                last_right = 0
        elif _input[i] == ",":
            i+=1
            continue
        else:
            if left == right:
                j = i
                while j < len(_input) and _input[j].isnumeric():
                    j += 1
                li.append(int(_input[i:j]))
                i = j
            
        i+=1
    return li

f = open("input.txt")
lines = f.readlines()

pos2 = 1
pos6 = 1
for line in lines:

    if line == "\n":
        continue
    
    line = line.replace("\n","")
    l1 = get_list_from_input(line[1:-1])
    l2 = [[2]]
    l6 = [[6]]
    #print(compare(l1,l2))

    #comp = compare(l1,l2)
    if compare(l1,l2) == -1:
        pos2 += 1

    if compare(l1,l6) == -1:
        pos6 += 1
    
print(pos2 * (pos6+1))