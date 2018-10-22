def reverse(lst):
	res = []
	i = len(lst) - 1

	while i >= 0:
	    letter = lst[i]
	    res.append(letter)
	    i = i -1
	return res



print reverse([4,3,2,1])
