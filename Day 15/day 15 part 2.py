f = open("input")
f = f.readlines()
s = set()
beacons = set()
test_row = 2000000
rows_to_test = 4000000
pivots = []


def add_pivot(to_add: tuple):
    if len(pivots) == 0:
        pivots.append(to_add)
        return

    i = 0
    while i < len(pivots):
        pivot = pivots[i]
        if to_add[0] >= pivot[0]:
            if to_add[0] > pivot[1]+1:
                if i == len(pivots) - 1:
                    pivots.append(to_add)
                i += 1
                continue
            if to_add[1] <= pivot[1]:
                return
            else:
                to_remove = pivot
                pivots.remove(pivot)
                to_add = (to_remove[0], to_add[1])
                if to_add not in pivots:
                    pivots.append(to_add)
                    i = 0
                continue
        elif to_add[1] <= pivot[1]:
            if to_add[1] < pivot[0]:
                if i == len(pivots) - 1:
                    pivots.append(to_add)
                i += 1
                continue
            if to_add[0] >= pivot[0]:
                return
            else:
                to_remove = pivot
                pivots.remove(pivot)
                to_add = (to_add[0], to_remove[1])
                if to_add not in pivots:
                    pivots.append(to_add)
                    i = 0
                continue
        elif to_add[0] < pivot[0] and to_add[1] > pivot[1]:
            pivots.remove(pivot)
            if to_add not in pivots:
                pivots.append(to_add)
                i = 0
            continue
        i += 1




for test_row in range(3250000,3300000):
    if test_row % 100000 == 0:
        print(test_row)

    pivots.clear()
    beacons.clear()
    for el in f:
        el = el.replace("Sensor at ", "").replace(" closest beacon is at ", "")
        el = el.replace("x=", "").replace("y=", "").replace(" ", "")
        el = el.split(":")
        sensor = [int(x) for x in el[0].split(",")]
        beacon = [int(x) for x in el[1].split(",")]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if beacon[1] == test_row:
            beacons.add((beacon[0], beacon[1]))

        if sensor[1] - distance <= test_row <= sensor[1] + distance:
            distance_to_objective = abs(test_row - sensor[1])
            new_pivot = (max(0, sensor[0] - distance + distance_to_objective),
                         min(sensor[0] + distance - distance_to_objective, rows_to_test))

            add_pivot(new_pivot)

    if len(pivots) >= 2:
        print(pivots, test_row)