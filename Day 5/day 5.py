from collections import deque
from inspect import stack

stacks = []

def populate_stack(line):
    for i in range(1,len(line),4):
        if line[i].isalpha():
            stacks[0 + int(i/4)].append(line[i])

def do_move_1(line):
    line = line.replace("move ","").replace("from ","").replace("to ","").replace("\n","")
    moves = line.split(" ")
    if len(line)==0:
        return
    #print("move " + moves[0] + " from " + moves[1] + " to " + moves[2])
    for i in range(int(moves[0])):
        move = stacks[int(moves[1])-1].pop()
        stacks[int(moves[2])-1].append(move)
        print("Moving " + move + " to " + str(int(moves[2])-1))

def do_move_2(line):
    line = line.replace("move ","").replace("from ","").replace("to ","").replace("\n","")
    moves = line.split(" ")
    if len(line)==0:
        return
    popped = ''
    for i in range(int(moves[0])):
        move = stacks[int(moves[1])-1].pop()
        popped += move

    while len(popped) > 0:
        move = popped[-1]
        stacks[int(moves[2])-1].append(move)
        popped = popped[:-1]
        #print("Moving " + move + " to " + str(int(moves[2])-1))


def part_1():
    f = open("input.txt")
    for i in range(9):
        stacks.append(deque())

    is_crate = True
    lines = f.readlines()
    for el in lines:
        if is_crate:
            if " 1   2   3   4   5   6   7   8   9 " in el:
                is_crate = False
                for stack in stacks:
                    stack.reverse()
            else:
                populate_stack(el)
        else:
            do_move_1(el)
        
    answer = ''
    for stack in stacks:
        answer += stack[len(stack)-1]
    print(answer)

def part_2():
    f = open("input.txt")
    for i in range(9):
        stacks.append(deque())

    is_crate = True
    lines = f.readlines()
    for el in lines:
        if is_crate:
            if " 1   2   3   4   5   6   7   8   9 " in el:
                is_crate = False
                for stack in stacks:
                    stack.reverse()
            else:
                populate_stack(el)
        else:
            do_move_2(el)
        
    answer = ''
    for stack in stacks:
        if len(stack) <= 0:
            answer += " "
        else:
            answer += stack[-1]
    print(answer)


#part_1()
part_2()
