from collections import deque

class Monkey:
    id = 0
    items = deque()
    operation = lambda x: x
    divisible_by = 1
    throw_to = {
        True : 0,
        False: 0
    }
    interacted = 0

    def __init__(self):
        items = deque()

f = open("input.txt")
lines = f.readlines()
monkeys = []

#init monkeys
for i in range(0, len(lines)+1, 7):
    monkey = Monkey()
    monkey.id = lines[i][7]
    
    #init items
    items = lines[i+1].replace("  Starting items: ","").split(", ")
    deq = deque()
    for item in items:
        deq.appendleft(int(item))
    monkey.items = deq
    
    #init operations 
    operation_line = lines[i+2].replace("  Operation: new = old ","")
    second_val = operation_line[2:]
    if operation_line[0] == "+":
        if "old" in second_val:
            fun = lambda x, second_val=second_val: x + x
            monkey.operation = fun
        else:
            fun = lambda x, second_val=second_val: x + int(second_val)
            monkey.operation = fun
    
    if operation_line[0] == "*":
        if "old" in second_val:
            fun = lambda x, second_val=second_val: x * x
            monkey.operation = fun
        else:
            fun = lambda x, second_val=second_val: x * int(second_val)
            monkey.operation = fun

    #init divisible
    divisible_by = int(lines[i+3].replace("  Test: divisible by ",""))
    monkey.divisible_by = divisible_by

    #init conditional operations
    true = int(lines[i+4].replace("    If true: throw to monkey ",""))
    false = int(lines[i+5].replace("    If false: throw to monkey ",""))
    monkey.throw_to = {
        True: true,
        False: false
    }

    #add to list
    monkeys.append(monkey)

num_rounds = 10000

for i in range(num_rounds):
    print(i)
    for monkey in monkeys:
        #print("Monkey ", monkey.id)
        while len(monkey.items) > 0:
            monkey.interacted += 1
            item = monkey.items.pop()

            #print("  Monkey inspects an item with a worry level of ", item)
            item = monkey.operation(item)
            #print("    Worry level is now ", item)
            item = int(item%9699690)
            #print("    After bored, worry level is now ", item)
            #print(item, " % ", monkey.divisible_by, item % monkey.divisible_by, item % monkey.divisible_by == 0)
            #print("    Sending to ", monkey.throw_to[(item % monkey.divisible_by) == 0])
            monkeys[monkey.throw_to[(item % monkey.divisible_by) == 0]].items.appendleft(item)
    
    #print("------------------------")
    
interactions = [monkey.interacted for monkey in monkeys]
max_val = max(interactions)
interactions.remove(max_val)
second_max = max(interactions)
print("\n")
print(max_val * second_max)