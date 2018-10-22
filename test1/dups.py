def dups(lst):
    res = []
    for number in range(len(lst)):
	if lst[number] in lst[number+1:] and lst[number] not in res:
		res += [lst[number]]
			

    return res


print dups([1,3,2,4,3,1,1])
