__author__ = 'luisfediaz'







N = 30002
from sys import  stdin
a = [None for i in range(N)]
coins = [5,10,25,50]

for line in stdin.readlines():
    for i in range(N):
        a[i] = 1
    for i in range(4):
        for j in range(coins[i], N):
            a[j]+= a[j-coins[i]]
    n = int(line)
    if(a[n] == 1):
        print("There is only %d way to produce %d cents change." %(a[n], n))
    else:
        print("There are %d ways to produce %d cents change."%(a[n], n))

