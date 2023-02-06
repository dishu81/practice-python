def factorial(x):
	num=1
	if x==0 or x==1:
		return num
	else:
		for i in range(1,x+1):
			num=num*i
		return num
 