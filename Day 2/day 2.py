def part_1():

    result_dict = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }

    pick_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    total = 0
    f = open("input.txt")
    for el in f:
        total = total + result_dict[el[0:-1]]
        total = total + pick_dict[el[-2]]

    print(total)

def part_2():

    result_dict = {
        "X" : 0,
        "Y" : 3,
        "Z" : 6
    }

    pick_points_dict = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    own_pick = {
        "A X": "Z",
        "A Y": "X",
        "A Z": "Y",
        "B X": "X",
        "B Y": "Y",
        "B Z": "Z",
        "C X": "Y",
        "C Y": "Z",
        "C Z": "X",
    }

    total = 0
    f = open("input.txt")
    for el in f:
        my_pick = own_pick[el[0:-1]]
        total = total + result_dict[el[-2]]
        total = total + pick_points_dict[my_pick]

    print(total)

part_1()
part_2()