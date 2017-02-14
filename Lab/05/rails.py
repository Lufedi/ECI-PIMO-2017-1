__author__ = 'luisfediaz'






from sys import stdin



line = stdin.readline()

while ( int(line) != 0):
    line = [int(x) for x in stdin.readline().split(" ")]
    trains = []
    while line[0] != 0:
        trains.append(line)
        line = [int(x) for x in stdin.readline().split(" ")]

    for i in range(len(trains)):
        train = trains[i]
        n  = len(train)
        stack = []
        target = 0
        for j in range(1, n + 1):
            stack.append(j)
            while not (len(stack) == 0) and stack[len(stack) - 1] == train[target] and j <= len(train):
                stack.pop()
                target= target + 1

        if(len(stack) == 0):
            print("Yes")
        else:
            print("No")
    print()

    line = stdin.readline()