def part_1():
    f = open("input.txt")
    max_count = 0
    current_count = 0

    for el in f:
        if el != "\n":
            current_count = current_count + int(el)
        else:
            max_count = max(current_count, max_count)
            current_count = 0

    print(max_count)

def part_2():
    f = open("input.txt")
    top_three = [0,0,0]
    current_count = 0

    for el in f:
        if el != "\n":
            current_count = current_count + int(el)
        else:
            for i in range(len(top_three)):
                if top_three[i] < current_count:
                    top_three[i] = current_count
                    current_count = 0
                    continue
            current_count = 0

    print(sum(top_three))

part_1()
part_2()