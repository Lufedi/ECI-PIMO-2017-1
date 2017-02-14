__author__ = 'luisfediaz'






from sys import  stdin
from collections import  deque
n = int(stdin.readline())
for i in range(n):
    lines = [int(x) for x in stdin.readline().strip().split(" ")]
    m = lines[0]
    pos = lines[1]
    vi = deque()
    lines = [int(x) for x in stdin.readline().strip().split(" ")]
    for j  in range(len(lines)):
        vi.append(lines[j])
    tot = 0

    while(True):
        ada =  False
        for j in range(len(vi)):
            if(vi[j] > vi[0]):
                ada = True
                break
        if( not ada):
            tot+=1
            vi.popleft()
        else:
            x = vi.popleft()
            vi.append(x)
        if(pos == 0 and  not ada):

            break
        pos-= 1
        if(pos < 0):
            pos = len(vi) - 1
    print(tot)




