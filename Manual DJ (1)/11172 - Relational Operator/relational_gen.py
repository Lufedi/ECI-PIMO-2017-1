from random import *

seed     = 12345
rand     = Random(seed)
min_val  = 1
max_val  = 100000001
test_cnt = 10000

tests = list()

while len(tests)!=test_cnt:
    a,b = [ rand.randrange(min_val,max_val) for i in range(2) ]
    tests.append('{0} {1}'.format(a,b))

print(len(tests))
print('\n'.join(tests))



