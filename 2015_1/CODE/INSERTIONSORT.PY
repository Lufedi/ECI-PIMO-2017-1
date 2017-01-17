def insertion_sort(A):
  n = len(A)
  for j in range(1, n):
    i,v = j-1,A[j]
    while i>=0 and A[i]>v:
      A[i+1] = A[i]
      i -= 1
    A[i+1] = v
