f = open("input")

s = set()
beacons = set()
test_row = 2000000
pivots = []


def add_pivot(to_add: tuple):
    if len(pivots) == 0:
        pivots.append(to_add)
        return

    for pivot in pivots:
        if to_add[0] >= pivot[0]:
            if to_add[1] <= pivot[1]:
                return
            else:
                to_remove = pivot
                pivots.remove(pivot)
                pivots.append((to_remove[0], to_add[1]))
        elif to_add[1] <= pivot[1]:
            if to_add[0] >= pivot[0]:
                return
            else:
                to_remove = pivot
                pivots.remove(pivot)
                pivots.append((to_add[0], to_remove[1]))


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
        new_pivot = (sensor[0] - distance + distance_to_objective, sensor[0] + distance - distance_to_objective)
        print(sensor, new_pivot, distance)
        add_pivot(new_pivot)

count = 0
print(pivots)
for p in pivots:
    count += (p[1] + 1 - p[0])
count -= len(beacons)
print(count)
