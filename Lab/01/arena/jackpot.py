__author__ = 'luisfediaz'




from sys import stdin

n  =  int(stdin.readline())
while(n != 0):
    sum  = max = i  = 0
    data = [int(c) for c in stdin.readline().split(" ")]
    for s in range(len(data)):
        sum+= data[s]
        if(sum < 0):
            sum = 0
        if(sum > max):
            max = sum
    if max > 0:
        print("The maximum winning streak is %d."%max)
    else:
        print("Losing streak.")
    n = int(stdin.readline())
