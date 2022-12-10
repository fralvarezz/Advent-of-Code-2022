f = open("input.txt")

cycle_values = [1]
instruction_takes = {
    "noop": 1,
    "addx": 2
}
visualization = "."*240

def visualize(visualization):
    print("",visualization[0:40],"\n",visualization[40:80],"\n",visualization[80:120],"\n",
    visualization[120:160],"\n",visualization[160:200],"\n",visualization[200:240],"\n",)



for line in f:
    if "noop" in line:
        cycle_values.append(cycle_values[-1])
    elif "addx" in line:
        x = int(line.replace("addx ", ""))
        for i in range(instruction_takes["addx"]):
            if i == 0:
                cycle_values.append(cycle_values[-1])
            elif i == instruction_takes["addx"] - 1:
                cycle_values.append(cycle_values[-1] + x)

count = 0
hor = 0
for i in range(0,len(cycle_values)):
    idx = i + (i%40)*40
    if i%40+1 >= cycle_values[i] and i%40+1 <= cycle_values[i]+2:
        visualization = visualization[:i] + "#" + visualization[i:]

visualize(visualization)            