from sys import stdin

def solve(a,b):
    ans = None
    if a<b:
        ans = '<'
    elif a==b:
        ans = '='
    else:
        ans = '>'
    return ans

def main():
    cases = int(stdin.readline())
    while cases!=0:
        a,b = [ int(x) for x in stdin.readline().split() ]
        print(solve(a,b))
        cases -= 1

main()
