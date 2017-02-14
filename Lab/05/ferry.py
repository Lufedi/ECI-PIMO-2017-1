__author__ = 'luisfediaz'







from sys import stdin
from collections import  deque
n = int(stdin.readline())



for c in  range(n):
    line = [x for x in stdin.readline().strip().split(" ")]
    l = int(line[0]) * 100
    m = int(line[1])
    left = deque()
    right = deque()
    for  i in range(m):
        line = [x for x in stdin.readline().strip().split(" ")]
        lc = int(line[0])
        bank = line[1]

        if bank == 'left':
            left.append(lc)
        else:
            right.append(lc)
    count = 0
    sd = 0
    while not len(left) == 0 or not len(right) == 0 :
        curLen = 0
        if(sd == 0):
            side = left
        else:
            side = right
        while not len(side) == 0:
            long = side[0]
            if(long + curLen <= l):
                curLen += long
                side.popleft()
            else:
                break

        count = count + 1
        sd = 1 -sd
    print(count)