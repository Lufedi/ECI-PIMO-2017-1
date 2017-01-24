__author__ = 'luisfediaz'




from sys import stdin



WHITE  = 0
GRAY =  1
BLACK  = 2
N =  21
tc = [None]*N;
t = [False] *N
cp = [False] *N
ans = 0
n =0


def backtrack(label):
    global ans
    global n
    global  t , cp , TC
    if(label == n):
        tmp = 0
        for i in range(n):
            if(t[i]):
                tmp += tc[i]
        if(tmp <= TC):
            if ans < tmp :
                ans = max(ans, tmp)
                for i in range (n):
                    cp[i] = t[i]
        return
    t[label] = True;
    backtrack(label+1);
    t[label] = False;
    backtrack(label+1);



for line in stdin.readlines():
    tc = []
    data = line.split(" ")
    TC = int(data[0])
    n = int(data[1])
    for i in range(n):
        tc.append( int(data[i+2]))
    ans = 0
    for i in range(n):
        cp[i] = False
    backtrack(0)
    for i in range (n):
        if(cp[i]):
            print("%d "%tc[i], end="")
    print('sum:%d'%ans)




