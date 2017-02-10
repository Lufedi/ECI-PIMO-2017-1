def fib(n):
   if n <= 2:
      return 1
   else:
      return fib(n-1) + fib(n-2)


dict = {}
dict[1] = 1
dict[2] = 1
dict[3] = 2
dict[(1,2,3,4)] = "weird"
dict["odd"] = 876

if 2 in dict:
   print("2 is a key!")
   print("its value is" + str(dict[2]))

dict2 = {1:1, 2:1, 3:2} # key:value pairs


fibTable = {1:1, 2:1}
def fib(n):
   if n <= 2:
      return 1
   if n in fibTable:
      return fibTable[n]
   else:
      fibTable[n] = fib(n-1) + fib(n-2)
      return fibTable[n]



