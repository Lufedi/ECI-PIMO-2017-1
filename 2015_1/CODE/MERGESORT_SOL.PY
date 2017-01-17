MAX = 1000
T = [ None for i in range(MAX) ]
cnt = 0

def merge(A, low, mid, hi):
  global T, cnt
  cnt = cnt+1
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

a = [5, 2, 4, 6, 1, 3, 10, 100, 9, 18, 19, 28, 33, 0, 78]
merge_sort(a, 0, len(a))
print(a, cnt)
"""
>>> [0, 1, 2, 3, 4, 5, 6, 9, 10, 18, 19, 28, 33, 78, 100] 14
"""
