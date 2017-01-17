MAX = 1000
T = [ None for i in range(MAX) ]

def merge(A, low, mid, hi):
  global T
  for i in range(low, hi): T[i] = A[i]
  l, r = low,mid
  for i in range(low, hi):
    if l<mid and r<hi:
      if T[l]<=T[r]:
        A[i],l = T[l],l+1
      else:
        A[i],r = T[r],r+1
    elif l==mid:
      A[i],r = T[r],r+1
    else:
      A[i],l = T[l],l+1

def merge_sort(A, low, hi):
  if low+1<hi:
    mid = low+((hi-low)//2)
    merge_sort(A, low, mid)
    merge_sort(A, mid, hi)
    merge(A, low, mid, hi)

