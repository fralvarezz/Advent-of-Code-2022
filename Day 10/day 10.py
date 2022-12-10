f = open("input.txt")

cycle_values = [1]
instruction_takes = {
    "noop": 1,
    "addx": 2
}


for line in f:

    if "noop" in line:
        cycle_values.append(cycle_values[-1])
    elif "addx" in line:
        x = int(line.replace("addx ", ""))
        print(x)
        for i in range(instruction_takes["addx"]):
            if i == 0:
                cycle_values.append(cycle_values[-1])
            elif i == instruction_takes["addx"] - 1:
                cycle_values.append(cycle_values[-1] + x)

print("-------------------")
count = 0
for i in range(19, len(cycle_values)+1,40):
        print(i, ": " ,cycle_values[i])
        count += (cycle_values[i]*(i+1))
print("-------------------")

print(count)
            