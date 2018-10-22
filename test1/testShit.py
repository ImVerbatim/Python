def shifted_by_one(s1,s2):
	length = len(s1)
	newS1 = list(s1)
	newS1_2 = list(s1)

    	num1 = newS1[length-1]
	newS1.remove(num1)
	newS1.insert(0,num1)
	
	num2 = newS1_2[0]
	newS1_2.remove(num2)
	newS1_2.insert(length,num2)

	answer1 = ''.join(newS1)
	answer2 = ''.join(newS1_2)

	print answer1 + ","+ answer2 

	if s2 == answer1 or s2 == answer2:
		return True
	else:
		return False
    	
print shifted_by_one('1234','4123')		
