def insertion_sort(A):
  n = len(A)
  cnt = 0
  for j in range(1, n):
    i,v = j-1,A[j]
    while i>=0 and A[i]>v:
      if i==3 and j==13: print("Valor:", A[i])
      cnt += 1
      A[i+1] = A[i]
      i -= 1
    A[i+1] = v
  print("Veces", cnt)

a = [5, 2, 4, 6, 1, 3, 10, 100, 9, 18, 19, 28, 33, 0, 78]
insertion_sort(a)
"""
Valor: 4
Veces 29
"""
