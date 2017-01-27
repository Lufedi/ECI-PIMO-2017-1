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



def destroy(stars):
	if len(stars) == 3:
		return stars[0] * stars[2]

	maior_produto = 0
	for index, _ in enumerate(stars[1:-1], start=1):
		produto = stars[index - 1] * stars[index + 1]
		if produto > maior_produto:
			sai = index
			maior_produto = produto



	stars.pop(sai)
	return (stars[sai-1]*stars[sai]) + destroy(stars)


