def cutHalf(lst):
  i = len(lst)
  size = i // 2
  newLst = []

  k = 0
  while k <= size:
    newLst += [lst[k]]
    k += 1

  return newLst


print cutHalf([1,2,3,4])
